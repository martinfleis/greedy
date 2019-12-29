Defining adjacency
==================


.. code:: ipython3

    import geopandas as gpd
    import pandas as pd
    import numpy as np
    from time import time
    import seaborn as sns
    import matplotlib.pyplot as plt

    from shapely.geometry import Point

.. code:: ipython3

    from greedy import greedy

.. code:: ipython3

    sns.set()

.. code:: ipython3

    polys = []
    for x in range(10):
        for y in range(10):
            polys.append(Point(x, y).buffer(0.5, cap_style=3))
    gdf = gpd.GeoDataFrame(geometry=polys)

.. code:: ipython3

    ax = gdf.plot(edgecolor='w')
    ax.set_axis_off()



.. image:: output_4_0.png


.. code:: ipython3

    libpysal based

.. code:: ipython3

    gdf['rook'] = greedy(gdf, sw='rook', min_colors=2)
    ax = gdf.plot('rook', edgecolor='w', categorical=True, cmap='Set3')
    ax.set_axis_off()



.. image:: output_6_0.png


.. code:: ipython3

    gdf['queen'] = greedy(gdf, sw='queen', min_colors=2)
    ax = gdf.plot('queen', edgecolor='w', categorical=True, cmap='Set3')
    ax.set_axis_off()



.. image:: output_7_0.png


.. code:: ipython3

    intersection based

.. code:: ipython3

    gdf['geos'] = greedy(gdf, min_distance=0, min_colors=2)
    ax = gdf.plot('geos', edgecolor='w', categorical=True, cmap='Set3')
    ax.set_axis_off()



.. image:: output_9_0.png


.. code:: ipython3

    gdf['dist1'] = greedy(gdf, min_distance=1, min_colors=2)
    ax = gdf.plot('dist1', edgecolor='w', categorical=True, cmap='Set3')
    ax.set_axis_off()



.. image:: output_10_0.png


.. code:: ipython3

    times = pd.DataFrame(index=['rook', 'queen', 'geos', 'dist1'])
    for number in range(10, 110, 10):
        print(number)
        polys = []
        for x in range(number):
            for y in range(number):
                polys.append(Point(x, y).buffer(0.5, cap_style=3))
        gdf = gpd.GeoDataFrame(geometry=polys)
        timer = []
        for run in range(5):
            s = time()
            colors = greedy(gdf, sw='rook')
            e = time() - s
            timer.append(e)
        times.loc['rook', number] = np.mean(timer)
        print('rook: ', np.mean(timer), 's; ', np.max(colors) + 1, 'colors')
        timer = []
        for run in range(5):
            s = time()
            colors = greedy(gdf, sw='queen')
            e = time() - s
            timer.append(e)
        times.loc['queen', number] = np.mean(timer)
        print('queen: ', np.mean(timer), 's; ', np.max(colors) + 1, 'colors')
        timer = []
        for run in range(5):
            s = time()
            colors = greedy(gdf, min_distance=0)
            e = time() - s
            timer.append(e)
        times.loc['geos', number] = np.mean(timer)
        print('geos: ', np.mean(timer), 's; ', np.max(colors) + 1, 'colors')
        timer = []
        for run in range(5):
            s = time()
            colors = greedy(gdf, min_distance=1)
            e = time() - s
            timer.append(e)
        times.loc['dist1', number] = np.mean(timer)
        print('dist1: ', np.mean(timer), 's; ', np.max(colors) + 1, 'colors')



.. parsed-literal::

    10
    rook:  0.01029210090637207 s;  4 colors
    queen:  0.006267690658569336 s;  4 colors
    geos:  0.15672893524169923 s;  4 colors
    dist1:  0.21950168609619142 s;  10 colors
    20
    rook:  0.01932358741760254 s;  4 colors
    queen:  0.019013690948486327 s;  4 colors
    geos:  0.5995094776153564 s;  4 colors
    dist1:  0.9240117073059082 s;  10 colors
    30
    rook:  0.04496006965637207 s;  4 colors
    queen:  0.04180002212524414 s;  4 colors
    geos:  1.3673813819885254 s;  4 colors
    dist1:  2.1132378578186035 s;  10 colors
    40
    rook:  0.08215422630310058 s;  4 colors
    queen:  0.08703317642211914 s;  4 colors
    geos:  2.4122870922088624 s;  4 colors
    dist1:  3.9358083724975588 s;  10 colors
    50
    rook:  0.13613815307617189 s;  4 colors
    queen:  0.1286477565765381 s;  4 colors
    geos:  3.7892502784729003 s;  4 colors
    dist1:  6.030300855636597 s;  10 colors
    60
    rook:  0.21495418548583983 s;  4 colors
    queen:  0.20560770034790038 s;  4 colors
    geos:  5.745699644088745 s;  4 colors
    dist1:  8.623000431060792 s;  10 colors
    70
    rook:  0.3028740882873535 s;  4 colors
    queen:  0.2708714485168457 s;  4 colors
    geos:  7.566797542572021 s;  4 colors
    dist1:  11.740409564971923 s;  10 colors
    80
    rook:  0.3894804954528809 s;  4 colors
    queen:  0.3736574649810791 s;  4 colors
    geos:  10.271010398864746 s;  4 colors
    dist1:  15.380718183517455 s;  10 colors
    90
    rook:  0.47423458099365234 s;  4 colors
    queen:  0.4377274990081787 s;  4 colors
    geos:  12.464200687408447 s;  4 colors
    dist1:  19.965694665908813 s;  10 colors
    100
    rook:  0.5873185157775879 s;  4 colors
    queen:  0.5612773895263672 s;  4 colors
    geos:  15.281956052780151 s;  4 colors
    dist1:  24.670071363449097 s;  10 colors


.. code:: ipython3

    times




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>10</th>
          <th>20</th>
          <th>30</th>
          <th>40</th>
          <th>50</th>
          <th>60</th>
          <th>70</th>
          <th>80</th>
          <th>90</th>
          <th>100</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>rook</th>
          <td>0.010292</td>
          <td>0.019324</td>
          <td>0.044960</td>
          <td>0.082154</td>
          <td>0.136138</td>
          <td>0.214954</td>
          <td>0.302874</td>
          <td>0.389480</td>
          <td>0.474235</td>
          <td>0.587319</td>
        </tr>
        <tr>
          <th>queen</th>
          <td>0.006268</td>
          <td>0.019014</td>
          <td>0.041800</td>
          <td>0.087033</td>
          <td>0.128648</td>
          <td>0.205608</td>
          <td>0.270871</td>
          <td>0.373657</td>
          <td>0.437727</td>
          <td>0.561277</td>
        </tr>
        <tr>
          <th>geos</th>
          <td>0.156729</td>
          <td>0.599509</td>
          <td>1.367381</td>
          <td>2.412287</td>
          <td>3.789250</td>
          <td>5.745700</td>
          <td>7.566798</td>
          <td>10.271010</td>
          <td>12.464201</td>
          <td>15.281956</td>
        </tr>
        <tr>
          <th>dist1</th>
          <td>0.219502</td>
          <td>0.924012</td>
          <td>2.113238</td>
          <td>3.935808</td>
          <td>6.030301</td>
          <td>8.623000</td>
          <td>11.740410</td>
          <td>15.380718</td>
          <td>19.965695</td>
          <td>24.670071</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    ax = times.T.plot()
    ax.set_ylabel('time (s)')
    ax.set_xlabel('# of polygons')
    locs, labels = plt.xticks()
    plt.xticks(locs, (times.columns ** 2), rotation='vertical')




.. parsed-literal::

    ([<matplotlib.axis.XTick at 0x1201bfdf0>,
      <matplotlib.axis.XTick at 0x11fece8e0>,
      <matplotlib.axis.XTick at 0x121743c40>,
      <matplotlib.axis.XTick at 0x11fe33610>,
      <matplotlib.axis.XTick at 0x11ffb10d0>,
      <matplotlib.axis.XTick at 0x1200f07c0>,
      <matplotlib.axis.XTick at 0x11f65a550>,
      <matplotlib.axis.XTick at 0x11f6520d0>,
      <matplotlib.axis.XTick at 0x11f652c10>,
      <matplotlib.axis.XTick at 0x11f61b6d0>],
     <a list of 10 Text xticklabel objects>)




.. image:: output_13_1.png


.. code:: ipython3

    ax = times.loc[['rook', 'queen']].T.plot()
    ax.set_ylabel('time (s)')
    ax.set_xlabel('# of polygons')
    locs, labels = plt.xticks()
    plt.xticks(locs, (times.columns ** 2), rotation='vertical')




.. parsed-literal::

    ([<matplotlib.axis.XTick at 0x11ff36a30>,
      <matplotlib.axis.XTick at 0x11ff36af0>,
      <matplotlib.axis.XTick at 0x11f5b9a90>,
      <matplotlib.axis.XTick at 0x11f5e9370>,
      <matplotlib.axis.XTick at 0x11f5e9d90>,
      <matplotlib.axis.XTick at 0x120053790>,
      <matplotlib.axis.XTick at 0x12005b250>,
      <matplotlib.axis.XTick at 0x12005bdf0>,
      <matplotlib.axis.XTick at 0x12002a970>,
      <matplotlib.axis.XTick at 0x12005b730>],
     <a list of 10 Text xticklabel objects>)




.. image:: output_14_1.png
