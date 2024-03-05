from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rhasan/__init__.py
from rhasan import __version__ as version

setup(
	name="rhasan",
	version=version,
	description="This R.Hassan Trading",
	author="TechVentures",
	author_email="safdar211@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
