from setuptools import find_packages,setup
from typing import List

setup (
    name = 'Fault detection',
    version='0.0.1',
    author='reshu',
    author_email='yadavreshu@199',
    install_requirements = ('requirements.txt'),
    packages=find_packages()
)