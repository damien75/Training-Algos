import os
from setuptools import setup, find_packages

version = os.environ.get('PACKAGE_VERSION', '0.0.0')

INSTALL_REQUIRES = []

TEST_REQUIRES = [
    'coverage'
]

EXTRAS_REQUIRE = {}


def setup_package():
    setup(
        name='Training Algorithms',
        version=version,
        author='Damien Goblot',
        description='Repo to gather interviews and algorithms trainings',
        packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        tests_require=TEST_REQUIRES,
        test_suite='nose.collector'
    )


if __name__ == '__main__':
    setup_package()
