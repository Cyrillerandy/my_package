from setuptools import setup, find_packages

setup(
    name = 'my_package',
    version = '0.1',
    packages = find_packages(exclude = ['tests']),
    license = 'COR',
    description = 'COR example pyhton package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = '#',
    author = 'cyrille_randy',
    author_email = 'omondi309@gmail.com'
)
