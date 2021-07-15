from setuptools import setup
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='iara',
    version='1.0.201',
    url='https://github.com/perseu912/iara',
    license='MIT License',
    author='Reinan Br',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='development mechanical statistical data science',
    description=u'Library for development on python works',
    packages=find_packages(),
    install_requires=['numpy','googlesearch','psutil','scipy','mechanicalsoup','pillow','tqdm','matplotlib','bs4','requests'],)