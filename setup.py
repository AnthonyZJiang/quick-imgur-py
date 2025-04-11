from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quickimgurpy",
    version="0.1.0",
    author="Anthony Z Jiang",
    author_email="anthony.jiang.github@outlook.com",
    description="A simple Python client for uploading images and videos to Imgur",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnthonyZJiang/quick-imgur-py",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.32.3",
        "python-dotenv>=1.1.0",
    ],
    extras_require={
    },
) 