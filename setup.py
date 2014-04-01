import sys
from setuptools import setup, find_packages

py26_dependency = []
if sys.version_info <= (2, 6):
    py26_dependency = [
        "argparse >= 1.2.1",
        "ordereddict"
    ]

setup(
    name="envplus",
    version="0.0.0",
    description="Combine your virtualenvs.",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3"
    ],
    keywords="virtualenv virtualenvwrapper virtual environments",
    author="Jeremy Singer-Vine",
    author_email="jsvine@gmail.com",
    url="http://github.com/jsvine/envplus/",
    license="MIT",
    packages=find_packages(exclude=["test",]),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        "virtualenvwrapper"
    ] + py26_dependency,
    tests_require=[],
    test_suite="test",
    entry_points={
        "console_scripts": [
            "envplus = envplus.cli:main",
        ]
    }
)
