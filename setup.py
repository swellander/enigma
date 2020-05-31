from setuptools import setup


setup(
    name='enigma',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'enigma=main:run'
        ]
    }
)
