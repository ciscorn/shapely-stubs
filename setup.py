from setuptools import setup

setup(
    name="shapely-stubs",
    version="0.1.0",
    packages=["shapely-stubs"],
    package_data={
        "shapely-stubs": ["*.pyi"],
    },
    install_requires=[
        "Shapely==2.0.1",
    ],
)
