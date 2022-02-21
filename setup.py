from setuptools import setup, find_packages

# Package meta-data.
NAME = "cdgator"
DESCRIPTION = "Public VNR package with most commonly used functions"
URL = "https://github.com/vnrag/test-helper-submodule.git"
VERSION = "0.1.0"
REQUIRES_PYTHON = ">=3.8"


# What packages are required for this module to be executed?
REQUIRED = []


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    license="MIT",
    packages=find_packages(exclude=("test",)),
    install_requires=REQUIRED,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
