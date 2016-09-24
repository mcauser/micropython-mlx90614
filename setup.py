from distutils.core import setup

setup(
    name='micropython-mlx90614',
    py_modules=['mlx90614'],
    version="1.0",
    description="Driver for MicroPython for the MLX90614 IR temperature sensor.",
    long_description="""\
This library lets you communicate with a MLX90614 IR temperature sensor.
""",
    author='Mike Causer',
    author_email='mcauser@gmail.com',
    classifiers = [
        'Development Status :: 6 - Mature',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)