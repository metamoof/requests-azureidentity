from setuptools import setup, find_packages

import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name = "requests-azureidentity",
    version = "0.0.2",
    author = "Giles Antonio Radford",
    author_email = "garadford@transcomashipping",
    description = "Azure Identity authentication support for Requests",
    url = "https://github.com/transcoma/requests-azureidentity",
    classifiers = [
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
    ],
    keywords= ["requests", "azure", "identity", "azure.identity", "OAuth", ],
    python_requires=">=3.6",
    install_requires=[
        "azure-identity>=1.6.0",
        "requests>=2.26.0",
    ],
)