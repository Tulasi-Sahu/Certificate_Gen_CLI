from setuptools import setup

setup(
    name='cgen',
    version='1.0',
    py_modules=[
        'main',
        'input_handler',
        'processor',
        'certificate_generator'
    ],
    install_requires=[
        'pillow',
        'pandas',
        'openpyxl'
    ],
    entry_points={
        'console_scripts': [
            'cgen=main:main',
        ],
    },
)
0