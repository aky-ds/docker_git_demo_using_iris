import os
from setuptools import setup, find_packages

def get_requirements(file_path):
    with open(file_path, 'r') as file:  # Open the file in read mode ('r')
        requires = file.readlines()  # Read lines from the file
        requires = [x.strip() for x in requires]  # Remove leading/trailing whitespace, including newlines
        if '-e .' in requires:
            requires.remove('-e .')  # Remove editable installation if present
    return requires

setup(
    name='ci/cd practice 1',
    version='0.1',
    author='Ayaz ul haq yousafzai',
    author_email='www.ayazkhan.com.21@gmail.com',
    description='A simple example of a Python package',
    packages=find_packages(),  # Use packages instead of setup_requires
    install_requires=get_requirements('requirements.txt')
)
