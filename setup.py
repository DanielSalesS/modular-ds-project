from setuptools import setup, find_packages

setup(
    name="modulards",
    version="0.1.0",
    author="Daniel Sales Santos",
    description="Centralizer of code and workflows for Data Science",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=open("requirements.txt", encoding="utf-8").read().splitlines(),
    python_requires=">=3.10",
)
