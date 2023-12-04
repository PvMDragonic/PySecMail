from setuptools import setup

settings = {
    "name": "PySecMail",
    "version": "1.0.0",
    "description": "A Python wrapper for 1secmail's temporary email API.",
    "url": "https://github.com/PvMDragonic/PySecMail",
    "author": "João Pedro Droval",
    "license": "MIT",
    "python_requires" : ">=3.9.10",
    "install_requires": [
        "requests>=2.31.0"
    ],
    "packages": [
        "PySecMail"
    ]
}

setup(**settings)