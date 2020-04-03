from setuptools import setup, find_packages


__version__ = '0.0.1'


develop_requires = [
    'autopep8',
    'flake8',
    'pep8-naming',
]


setup(
    name='pyautocast',
    version=__version__,
    author='ctgk',
    author_email='r1135nj54w@gmail.com',
    url='https://github.com/ctgk/pyautocast',
    description='Automatic function arguments casting',

    packages=find_packages(exclude=('test*',)),
    python_requires=">=3.7",
    extras_require={"develop": develop_requires},

    test_suite="tests",
)
