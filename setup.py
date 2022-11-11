from setuptools import find_packages, setup

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name='project-example',
    packages=['project-example'],
    package_dir={'project-example': 'src'},
    version='0.1.0',
    description='my desc',
    author='Yaron',
    author_email="author@example.com",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
)
