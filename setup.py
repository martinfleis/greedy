import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="greedy",
    version="0.1.1",
    author="Martin Fleischmann",
    author_email="martin@martinfleischmann.net",
    description="Greedy (topological) coloring for GeoPandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/martinfleis/greedy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["geopandas", "networkx", "libpysal"],
)
