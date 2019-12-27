import operator
import sys
from collections import defaultdict

import libpysal
import networkx as nx
import pandas as pd

STRATEGIES = nx.algorithms.coloring.greedy_coloring.STRATEGIES.keys()


def balanced(features, sw, balance="count", min_colors=4):
    """
    get balanced colours - ported from QGIS, enhanced.

    Original code: (C) 2017, Nyall Dawson

    add docstring
    """
    feature_colors = {}
    # start with minimum number of colors in pool
    color_pool = set(range(min_colors))

    # calculate count of neighbours
    neighbour_count = sw.cardinalities

    # sort features by neighbour count - we want to handle those with more neighbours first
    sorted_by_count = [
        feature_id
        for feature_id in sorted(
            neighbour_count.items(), key=operator.itemgetter(1), reverse=True
        )
    ]
    # counts for each color already assigned
    color_counts = defaultdict(int)
    color_areas = defaultdict(float)
    for c in color_pool:
        color_counts[c] = 0
        color_areas[c] = 0

    for (feature_id, n) in sorted_by_count:
        # first work out which already assigned colors are adjacent to this feature
        adjacent_colors = set()
        for neighbour in sw.neighbors[feature_id]:
            if neighbour in feature_colors:
                adjacent_colors.add(feature_colors[neighbour])

        # from the existing colors, work out which are available (ie non-adjacent)
        available_colors = color_pool.difference(adjacent_colors)

        feature_color = -1
        if len(available_colors) == 0:
            # no existing colors available for this feature, so add new color to pool and repeat
            min_colors += 1
            return balanced(features, sw, balance, min_colors)
        else:
            if balance == "count":
                # choose least used available color
                counts = [
                    (c, v) for c, v in color_counts.items() if c in available_colors
                ]
                feature_color = sorted(counts, key=operator.itemgetter(1))[0][0]
                color_counts[feature_color] += 1
            elif balance == "area":
                areas = [
                    (c, v) for c, v in color_areas.items() if c in available_colors
                ]
                feature_color = sorted(areas, key=operator.itemgetter(1))[0][0]
                color_areas[feature_color] += features.iloc[feature_id].geometry.area
            elif balance == "centroid":
                min_distances = {c: sys.float_info.max for c in available_colors}
                this_feature_centroid = features.iloc[feature_id].geometry.centroid

                # find features for all available colors
                other_features = {
                    f_id: c
                    for (f_id, c) in feature_colors.items()
                    if c in available_colors
                }

                # loop through these, and calculate the minimum distance from this feature to the nearest
                # feature with each assigned color
                for other_feature_id, c in other_features.items():

                    other_geometry = features.iloc[other_feature_id].geometry
                    other_centroid = other_geometry.centroid

                    distance = this_feature_centroid.distance(other_centroid)
                    if distance < min_distances[c]:
                        min_distances[c] = distance

                # choose color such that minimum distance is maximised! ie we want MAXIMAL separation between
                # features with the same color
                feature_color = sorted(
                    min_distances, key=min_distances.__getitem__, reverse=True
                )[0]

            elif balance == "distance":
                min_distances = {c: sys.float_info.max for c in available_colors}
                this_feature = features.iloc[feature_id].geometry

                # find features for all available colors
                other_features = {
                    f_id: c
                    for (f_id, c) in feature_colors.items()
                    if c in available_colors
                }

                # loop through these, and calculate the minimum distance from this feature to the nearest
                # feature with each assigned color
                for other_feature_id, c in other_features.items():

                    other_geometry = features.iloc[other_feature_id].geometry

                    distance = this_feature.distance(other_geometry)
                    if distance < min_distances[c]:
                        min_distances[c] = distance

                # choose color such that minimum distance is maximised! ie we want MAXIMAL separation between
                # features with the same color
                feature_color = sorted(
                    min_distances, key=min_distances.__getitem__, reverse=True
                )[0]

        feature_colors[feature_id] = feature_color

    return feature_colors


def geos_sw(features, min_distance=0, silence_warnings=False):
    """
    generate SW based on intersections
    add docstring
    """
    neighbors = {}

    sindex = features.sindex

    if min_distance > 0:
        features = features.copy()
        features["geometry"] = features.geometry.buffer(min_distance / 2, 5)

    for i, (ix, f) in enumerate(features.iterrows()):

        g = f.geometry

        possible_matches_index = list(sindex.intersection(g.bounds))
        possible_matches_index.remove(i)
        possible_matches = features.iloc[possible_matches_index]
        precise_matches = possible_matches.loc[possible_matches.intersects(g)]

        neighbors[ix] = list(precise_matches.index)

    return libpysal.weights.W(neighbors, silence_warnings=silence_warnings)


def greedy(
    gdf,
    strategy="balanced",
    balance="count",
    min_colors=4,
    sw="queen",
    min_distance=None,
    silence_warnings=False,
):
    """
    main greedy function
    add docstring

    Parameters
    ----------
    gdf : GeoDataFrame
        GeoDataFrame
    strategy : str (default 'balanced')
        coloring strategy

        explain
    balance : str (default 'count')
        if strategy is 'balanced', determine the method of color balancing

        explan
    min_colors: int (default 4)
        if strategy is 'balanced', define the minimal number of colors to be used

    sw : 'queen', 'rook' or libpysal.weights.W
        spatial weights

    min_distance : float
        minimal distance between colors

        explain slower algorithm

    silence_warnings : bool (default True)
        silence lilbpysal warnings (if min_distance is set)

    Examples
    --------
    >>>
    """
    if min_distance is not None:
        sw = geos_sw(gdf, min_distance=min_distance, silence_warnings=silence_warnings)

    if not isinstance(sw, libpysal.weights.W):
        if sw == "queen":
            sw = libpysal.weights.Queen.from_dataframe(gdf)
        elif sw == "rook":
            sw = libpysal.weights.Rook.from_dataframe(gdf)

    if strategy == "balanced":
        return pd.Series(
            balanced(gdf, sw, balance=balance, min_colors=min_colors), index=gdf.index
        )

    elif strategy in STRATEGIES:
        color = nx.greedy_color(sw.to_networkx(), strategy=strategy)
        return pd.Series(color, index=gdf.index)

    else:
        raise ValueError("{} is not a valid strategy.".format(strategy))
