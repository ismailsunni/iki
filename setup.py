import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='iki',
    version='0.1.0',
    author='Ismail Sunni',
    author_email='imajimatika@gmail.com',
    description='Javanese version of import this.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/ismailsunni/iki',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education"]
        )
