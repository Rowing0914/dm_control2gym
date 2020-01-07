# followed this tutorial
# https://packaging.python.org/tutorials/packaging-projects/

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dm_control2gym",
    version="0.0.1",
    author="Norio Kosaka",
    author_email="kosakaboat@gmail.com",
    description="dm_control suite for OpenAI Gym env",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rowing0914/dm_control2gym",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
