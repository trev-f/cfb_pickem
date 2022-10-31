from setuptools import find_packages, setup

setup(
    name='cfb_pickem',
    packages=find_packages(),
    version='0.1.0',
    description='Pick college football games against the spread.',
    author='Trevor F. Freeman',
    license='MIT',
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'cfb-pickem = cfb_pickem.cli:cli',
        ],
    },
)
