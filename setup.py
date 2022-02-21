from setuptools import setup, find_packages

setup(
    name="cdgator",
    version="0.0.1",
    author="VNR",
    description="Public VNR package with most commonly used functions",
    url="https://github.com/vnrag/test-helper-submodule.git",
    package_dir={"": "cdgator"},
    packages=find_packages(where="cdgator", exclude=("test",)),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
