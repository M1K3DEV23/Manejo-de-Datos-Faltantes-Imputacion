#!/usr/bin/env python3

import os

from setuptools import find_packages, setup


def readme() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    return open(os.path.join(os.path.dirname(__file__), "README.md")).read()


setup(
    name="imputacion_packages",
    version="1.0",
    author='M1K3DEV23',
    author_email="mikery2310@outlook.com",
    description="Estimar los valores ausentes con base en los valores validos de otras variables y/o casos de muestra.",
    python_requires=">=3",
    license='MIT',
    url="",
    packages=find_packages(),
    long_description=readme(),
)
