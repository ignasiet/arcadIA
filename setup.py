from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("obj/action.pyx", language_level=3)
)