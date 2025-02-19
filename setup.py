from setuptools import find_packages,setup
# from typing import list 

setup(
    name="sensor",
    version="0.0.1",
    author="Kiran Singh",
    author_email="2241018@sliet.ac.in",
    packages=find_packages(),
    install_requires=["pymongo"]
)