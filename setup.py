from distutils.core import setup
from setuptools import find_packages

setup(
    name="math-quiz",
    version="0.1",
    author="C.Brueckner",
    author_email="chris.brueckner@fau.de",
    packages=find_packages(),
    install_requires=["random", "unittest"],
)