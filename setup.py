from setuptools import setup, find_packages


with open('README.rst', 'r') as f:
    readme = f.read()

with open('LICENSE', 'r') as f:
    license = f.read()


setup(
    name='timpani',
    version='0.0.1',
    description='Test impact analysis for python projects',
    long_description=readme,
    author='Thomas Dane',
    author_email='thomasgdane@gmail.com',
    url='https://github.com/thomasgdane/timpani',
    license=license,
    package=find_packages(exclude=('tests', 'docs'))
)
