import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup

setup(
    name='micropython-mlx90614',
    py_modules=['mlx90614'],
    version='1.0.0',
    description='MicroPython library for the MLX90614 IR temperature sensor.',
    long_description='This library lets you communicate with a MLX90614 IR temperature sensor.',
    keywords='mlx90614 infrared temperature micropython',
    url='https://github.com/mcauser/micropython-mlx90614',
    author='Mike Causer',
    author_email='mcauser@gmail.com',
    maintainer='Mike Causer',
    maintainer_email='mcauser@gmail.com',
    license='MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'License :: OSI Approved :: MIT License',
    ],
)