"""
Make the project installable via pip. the project meta data are present here.
"""

import setuptools
from setuptools import setup

# Read the readme file, which will be our long description.
with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

version: str = "1.0.0"
repo_name: str = "Text-summarization-nlp"
git_hub_username: str = "pavi-ninjaac"
author_name: str = "Pavithra Devi M"
author_email = "pavipd495@gmail.com"
package_name: str = "TextSummarization"


# setup the project.
setup(
    name=package_name,
    version=version,
    author=author_name,
    author_email=author_email,
    description="A small package for text summarization",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{git_hub_username}/{repo_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{git_hub_username}/{repo_name}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8"
)
