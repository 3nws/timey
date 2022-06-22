from os.path import abspath, join

from setuptools import setup

with open(abspath(join(__file__, "..", "timey", "version.py"))) as f:
    data = f.read().split("=")[-1]

version = float(data.strip().replace('"', ""))

setup(
    name="timey",
    version=str(version),
    packages=["timey"],
    url="https://github.com/3nws/timey",
    license="MIT",
    author="3nws",
    description="A simple(garbage and completely unnecessary but practice) async API wrapper for the [TimeAPI](https://www.timeapi.io) written in python.",
    python_requires=">=3.8",
)
