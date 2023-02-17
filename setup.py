from setuptools import setup, find_packages

setup(
    name="Lie",
    version="1.0.1",
    description="Classes implementing Lie Groups and Algebras",
    author="Varun Madabushi",
    packages=find_packages(),
    install_requires=["numpy", "scipy", "matplotlib"],
)
