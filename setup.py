from setuptools import setup, find_packages

setup(
    name='Certificate_generator',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'pandas',
        'fpdf',
        'openpyxl'  # for reading .xlsx files
    ],
    entry_points={
        'console_scripts': [
            'Certificate_generator = Certificate_generator.generate_certificate:main',
        ],
    },
)
