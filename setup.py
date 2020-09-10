"""
Publish a new version:

$ git tag X.Y.Z -m "Release X.Y.Z"
$ git push --tags

$ pip install --upgrade twine wheel
$ python setup.py sdist bdist_wheel --universal
$ twine upload dist/*
"""
import codecs

from setuptools import setup

SCHE_VERSION = "1.0a3"
SCHE_DOWNLOAD_URL = "https://github.com/yifeikong/sche/tarball/" + SCHE_VERSION


def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, "r", "utf8") as f:
        return f.read()


setup(
    name="sche",
    packages=["sche"],
    version=SCHE_VERSION,
    description="Job scheduling for humans.",
    long_description=read_file("README.rst"),
    license="MIT",
    author="Yifei Kong",
    author_email="kong@yifei.me",
    scripts=["bin/sche"],
    url="https://github.com/yifeikong/sche",
    download_url=SCHE_DOWNLOAD_URL,
    keywords=[
        "schedule",
        "periodic",
        "jobs",
        "scheduling",
        "clockwork",
        "cron",
        "scheduler",
        "job scheduling",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Natural Language :: English",
    ],
    python_requires=">=3.6",
)
