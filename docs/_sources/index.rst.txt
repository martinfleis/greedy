.. greedy documentation master file, created by
   sphinx-quickstart on Sat Dec 28 18:45:08 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

greedy's documentation
======================

.. image:: https://travis-ci.org/martinfleis/greedy.svg?branch=master
    :target: https://travis-ci.org/martinfleis/greedy

.. image:: https://codecov.io/gh/martinfleis/greedy/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/martinfleis/greedy

``greedy`` a Python package which brings topological (greedy) coloring to GeoPandas.
Several coloring strategies all accessible using one line of code::

    gdf['colors'] = greedy(gdf)

.. image:: images/getting_started/output_7_0.png

Install greedy using ``conda`` from  ``conda-forge``::

    conda install -c conda-forge greedy

Or from PyPI using ``pip``::

    pip install greedy



.. toctree::
   :maxdepth: 2
   :caption: Documentation:

   install
   getting_started
   adjacency
   strategies
   api
   GitHub <https://github.com/martinfleis/greedy>



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
