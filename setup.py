from setuptools import setup, find_packages

with open ('requirements.txt') as f:
    required = f.read().splitlines()

with open('README.md') as f:
    long_description = f.read()

setup(
    name='plants-family',
    version='0.0.1',
    packages=find_packages(),
    install_requires=required,
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True
)
