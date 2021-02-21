#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import path
from codecs import open

setup(
    name='gctools',
    version='0.1',
    description='A set of analysis for riding activities that complement GoldenCheetah',
    url='',
    author='David Vazquez Garcia',
    author_email='davidvazquez.gijon@gmail.com',
    license='MIT',
    classifiers=[
    ],
    keywords='',
    #packages=[],
    packages=find_packages(exclude=[]),
    install_requires=['jupyter', 'notebook', 'nbconvert', 'ipython[all]',
        'pyyaml', 'pandas'],
    dependency_links=[],
    platforms='any',
    #package_files=[],
    #data_files=[],
    #include_package_data=True,
    entry_points={
        'console_scripts': [
            # 'gctools_activity_summary = gctools.activity_csv_generator:main',
        ],
    },
)
