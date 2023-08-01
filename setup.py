from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    """Return requirements from requirements.txt file"""
    with open(file_path) as f:
        requirements = f.readlines()
        requirements=[req.replace("\\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Tahseen",
    author_email="t.samoon@yahoo.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
