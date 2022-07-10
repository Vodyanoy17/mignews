from setuptools import setup, find_packages

__version__ = "0.0.0"

# try:
#     from semantic_release import setup_hook

#     setup_hook(sys.argv)
# except ImportError:
#     pass


print(find_packages())
setup(
    name="mignews",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/Vodyanoy17/mignews/blob/main/setup.cfg",
    license="BSD License",
    author="Gregory Vinopal",
    author_email="gregory.vinopal@intel.com",
    description="mignews",
    python_requires=">=3.6",
    install_requires=["semantic_release", "python-semantic-release"],
)
