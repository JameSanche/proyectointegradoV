from setuptools import setup, find_packages

setup(
    name='proyectointegradoV',
    version='0.1',
    author='James Sanchez',
    description='Proyecto Integrado V',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'pandas',
        'openpyxl',
        'requests',
        'beautifulsoup4',
        'scikit-learn',
        'numpy',
        'matplotlib',
        'seaborn',
        'statsmodels'
    ],
)
