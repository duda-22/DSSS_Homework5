from distutils.core import setup
from setuptools import find_packages

setup(
      name= "snowflake",
      version= "0.1",
      author= "duda-22",
      author_email= "edith.gramotke@fau.de",
      packages=find_packages(),
      install_requires= ["numpy", "turtles"],
)