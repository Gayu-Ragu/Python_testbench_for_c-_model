from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension

setup(name="accel", ext_modules=[Pybind11Extension("accel",["accel.cpp"])])
