# -*- coding: utf-8 -*-
import os

from setuptools import setup

VERSION = "1.0.0"


def readme(*paths):
    with open(os.path.join(*paths), "r") as f:
        return f.read()


def requirements(*paths):
    with open(os.path.join(*paths), "r") as f:
        return list(line.strip() for line in f.readlines() if line.strip() != "")


setup(
    name="slogger",
    packages=["slogger"],
    version=VERSION,
    description="Slack Logging extending the logging module",
    long_description=readme("README.rst"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Communications :: Chat",
        "Topic :: Office/Business :: Groupware",
    ],
    url="https://github.com/jacobmaynard/slogger",
    download_url="https://github.com/jacobmaynard/slogger/archive/{v}.tar.gz".format(
        v=VERSION
    ),
    author="Jacob Maynard",
    author_email="jake@maynard-las.com",
    keywords=["slack", "logging"],
    install_requires=requirements("requirements.txt"),
    include_package_data=True,
    zip_safe=False,
)
