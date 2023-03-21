from setuptools import find_packages
from setuptools import setup

setup(
    name='apriltag_msgs',
    version='2.0.0',
    packages=find_packages(
        include=('apriltag_msgs', 'apriltag_msgs.*')),
)
