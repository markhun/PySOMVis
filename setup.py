from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="PySOMVis",
    version="0.0.1",
    author="Sergei Mnishko",
    author_email="sergei.mnishko@gmail.com",
    packages=(find_packages(where=".")),
    url="https://github.com/smnishko/PySOMVis",
    license="LICENSE.txt",
    description="PySOMVis is an open-source Python-based GUI implementation for analyzing trained SOMs. It provides a wide range of different visualizations for the SOM, such as Chessboard Visualization, Clustering approach, Component Plane, D-Matrix, Hit Histogram, Metro Map, Neighborhood Graphs, Pie Chart, Smoothed Data Histogram, U-Matrix, U*-Matrix, P-Matrix, Quantization Error, SOMStreamVis",
    long_description=open("README.md").read(),
    install_requires=required,
)
