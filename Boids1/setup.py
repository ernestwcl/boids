from setuptools import setup, find_packages

setup(
    name = "Boids",
    version = "1.0",
    packages = find_packages(exclude=['*test']),
    description = "Boid flocking simulation",
    author = "Ernest Lo",
    author_email = "ernest.lo.15@ucl.ac.uk",
    url = "https://github.com/ernestwcl/boids",
    scripts = ['Boids/command.py'],
    install_requires = ['argparse','numpy','matplotlib']
)