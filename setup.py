import os

from setuptools import setup, find_packages

MODULE_TITLE = "soundpi"
MODULE_VERSION = "0.0.1"
MODULE_DESCRIPTION = ""
MODULE_PYTHON_REQUIRES = ">=3.11"
MODULE_LONG_DESCRIPTION = ""
MODULE_DIRECTORY_SOURCE = "soundpi"
MODULE_DIRECTORY_SAMPLE = "examples"
MODULE_DIRECTORY_RESOURCES = "resources"
MODULE_SOURCE = []
MODULE_SAMPLE_SOURCE = []
MODULE_SAMPLE_RESOURCES = []

for dirpath, dirnames, filenames in os.walk(MODULE_DIRECTORY_SAMPLE):
    for filename in filenames:
        MODULE_SAMPLE_SOURCE.append(os.path.join(dirpath, filename))

for dirpath, dirnames, filenames in os.walk(MODULE_DIRECTORY_RESOURCES):
    for filename in filenames:
        MODULE_SAMPLE_RESOURCES.append(os.path.join(dirpath, filename))

for dirpath, dirnames, filenames in os.walk(MODULE_DIRECTORY_SAMPLE):
    for filename in filenames:
        if filename.endswith(".py"):
            MODULE_SOURCE.append(os.path.join(dirpath, filename))

with open("README.md", 'r', encoding='utf-8') as f:
    MODULE_LONG_DESCRIPTION += f.read()

setup(
    name=MODULE_TITLE,
    version=MODULE_VERSION,
    description=MODULE_DESCRIPTION,
    python_requires=MODULE_PYTHON_REQUIRES,

    author='SealtielFreak',
    author_email="sealtielfreak@yandex.com",

    license="MIT",

    url="https://github.com/SealtielFreak/soundpi",
    packages=find_packages(),
    scripts=MODULE_SOURCE,

    long_description=MODULE_LONG_DESCRIPTION,
    long_description_content_type="text/markdown",

    data_files=[
        ("", ["LICENSE", "README.md"]),
        ("docs", ["requirements.txt"]),
        (MODULE_DIRECTORY_SAMPLE, MODULE_SAMPLE_SOURCE),
        (MODULE_DIRECTORY_RESOURCES, MODULE_SAMPLE_RESOURCES),
    ],
)
