from setuptools import setup

setup(
    name='checkifup',
    version='0.1.0',
    py_modules=['checkifup'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'checkifup = checkifup:cli',
        ],
    },
)