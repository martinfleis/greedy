# greedy
[![Build Status](https://travis-ci.org/martinfleis/greedy.svg?branch=master)](https://travis-ci.org/martinfleis/greedy) [![codecov](https://codecov.io/gh/martinfleis/greedy/branch/master/graph/badge.svg)](https://codecov.io/gh/martinfleis/greedy)

## Introduction
Greedy (topological) coloring for GeoPandas

`greedy` is a Python package which brings topological (greedy) coloring to [GeoPandas](http://geopandas.org).
It offers several coloring strategies, all accessible using one line of code::

```py
gdf['colors'] = greedy(gdf)
```

![alt text](https://raw.githubusercontent.com/martinfleis/greedy/images/getting_started/output_7_0.png)

## Documentation
Documentation of `greedy` is available at [martinfleis.github.io/greedy](https://martinfleis.github.io/greedy/).


## Install
You can install `momepy` using Conda from `conda-forge` (recommended):

    conda install -c conda-forge greedy

or from PyPI using `pip`:

    pip install greedy

See the [installation instructions](https://martinfleis.github.io/greedy/install.html) for detailed instructions.

---
Copyright (c) 2017 - 2019 Martin Fleischmann, Nyall Dawson
