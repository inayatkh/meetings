from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in meetings/__init__.py
from meetings import __version__ as version

setup(
	name="meetings",
	version=version,
	description="Arrange Various Meetings at various avenues",
	author="Dr Inayat Khan",
	author_email="inayatkh@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
