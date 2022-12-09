import setuptools
with open("Readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"

REPO_NAME = "IPYNBrenderer"
AUTHOR_USERNAME = "abhilashajay-dev"
SRC_REPO = "IPYNBrenderer"
AUTHOR_EMAIL = "abhilashajay123@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description = "A package to render IPYNB files",
    long_description=long_description,
    long_description_content="text/markdown",
    url = f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)