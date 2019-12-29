Install
=======

.. note::

    Greedy is under development, instructions below do not apply at this moment.

Installing ``greedy`` is straightforward using both ``pip`` and ``conda``.

Greedy is a small extension of GeoPandas. That can be a bit complicated to install
in some cases. For details on installing GeoPandas, please refer to `GeoPandas
installation instructions <http://geopandas.org/install.html>`__.

Install via Conda
-----------------

As ``greedy`` is dependent on `geopandas`_ and other spatial packages, we recommend
to install all dependencies via `conda`_ from `conda-forge`_::

    conda install -c conda-forge greedy

Conda should be able to resolve any dependency conflicts and install greedy
together with all necessary dependencies.

If you do not have `conda-forge`_ in your conda channels, you can add it using::

    conda config --add channels conda-forge

To ensure that all dependencies will be installed from `conda-forge`_, we recommend
using strict channel priority::

    conda config --env --set channel_priority strict

.. note::

    We strongly recommend to install everything from the *conda-forge* channel.
    Mixture of conda channels or conda and pip packages can lead to import problems.


Creating a new environment for greedy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to make sure, that everything will work as it should, you can create
a new conda environment for greedy. Assuming we want to create a new environment
called ``greedy_env``::

    conda create -n greedy_env
    conda activate greedy_env
    conda config --env --add channels conda-forge
    conda config --env --set channel_priority strict
    conda install greedy


Install via pip
---------------

greedy is also available on PyPI, but ensure that all dependencies are properly
installed before installing greedy. Some C dependencies are causing problems with
installing using pip only::

    pip install greedy

Install from the repository
---------------------------

If you want to work with the latest development version of greedy, you can do so
by cloning `GitHub repository <https://github.com/martinfleis/greedy>`__ and
installing greedy from local directory::

    git clone https://github.com/martinfleis/greedy.git
    cd greedy
    pip install .

Alternatively, you can install the latest version directly from GitHub::

    pip install git+git://github.com/martinfleis/greedy.git

Installing directly from repository might face the same dependency issues as
described above regarding installing using pip. To ensure that environment is
properly prepared and every dependency will work as intended, you can install
them using conda before installing development version of greedy::

    conda install -c conda-forge geopandas networkx libpysal


Dependencies
------------

Required dependencies:

- `geopandas`_
- `libpysal`_ (>= 4.1.0)
- `networkx`_


.. _geopandas: https://geopandas.org/

.. _libpysal: https://libpysal.readthedocs.io

.. _networkx: http://networkx.github.io

.. _conda-forge: https://conda-forge.org/

.. _conda: https://conda.io/en/latest/
