from setuptools import setup, find_packages

setup(
    name = "Boids",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['Boids/command.py'],
    install_requires = ['argparse','numpy','matplotlib']
)