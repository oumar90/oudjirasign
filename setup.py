from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README
 

setup(
    name="oudjirasign",
    version="1.0.0",
    description="oudjirasign est un module python de signature électronique..",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/oumar90/oudjirasign",
    author="Oumar Djimé Ratou",
    author_email="oudjira90@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["meteo"],
    include_package_data=True,
    install_requires=["pycrypto==2.6.1"],
    entry_points={
        "console_scripts": [
            "oudjirasign=oudjira_sign.oudjirasign:main",
        ]
    },
)