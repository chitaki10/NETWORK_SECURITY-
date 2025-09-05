from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return the list of requirements.
    """
    requirements_list: List[str] = []
    try:
        with open("requirements.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and '-e .'
                if requirement and not requirement.startswith("-e"):
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirements_list

setup(
    name="Network_Security",
    version="0.0.1",
    author=" charan ",
    author_email="chitakin876@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)