from setuptools import setup, find_packages

setup(
    name="synthra",  # Replace with your desired package name
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "colorama>=0.4.6",
    ],
    description="A simple logging module for Python",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="x2sadddDM",
    author_email="x2saddddm@gmail.com",
    url="https://github.com/x2saddDM/synthra-logger",
)
