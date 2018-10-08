import os
from codecs import open
from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements
here = os.path.abspath(os.path.dirname(__file__))

install_requirements = parse_requirements('requirements.txt', session=False)
requirements = [str(ir.req) for ir in install_requirements]

setup(
    name='sacred_helper',
    version='0.0.1',
    description='Small helper to retrieve past Sacred experiments',
    author="Romain Sabathe",
    keywords='sacred experiment machine learning',
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={},
    include_package_data=True,
    install_requires=requirements,
)

