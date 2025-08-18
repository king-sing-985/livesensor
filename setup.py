from setuptools import find_packages, setup
from typing import List

def get_requiremennts()->list[str]:

    requirements_list=list[str]=[]

    return requirements_list

setup(
    name = 'Sensor',
    version = "0.0.1",
    author = "Kiran",
    author_email='2241018@sliet.ac.in',
    packages=find_packages(),
    install_requires= get_requiremennts() , #["pymongo"]

)