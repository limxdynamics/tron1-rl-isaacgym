from setuptools import find_packages
from distutils.core import setup

setup(
    name="legged_gym",
    version="1.0.0",
    author="Hongxi Wang, LimX Dynamics",
    license="BSD-3-Clause",
    packages=find_packages(),
    url="https://github.com/limxdynamics/tron1-rl-isaacgym",
    description="Isaac Gym RL environments for LimX TRON1 (point-foot, sole-foot, wheel-foot), based on legged_gym by Nikita Rudin, ETH Zurich",
    install_requires=["isaacgym", "matplotlib"],
)
