import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spotify-pkg",
    version="0.0.1",
    author="Daniel Aranias",
    author_email="danielaranias@gmail.com",
    description="INteracting with Spotify to do cool thing to make your experience better",
    long_description=long_description,
    long_description_content_type="",
    url="https://github.com/danielaranias/Spotify.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)