from setuptools import setup

setup(
    name = 'jenkins-python',
    version = '0.1',
    url = 'https://github.com/tuomas-kulmala/jenkins-python.git',
    author = 'Tuomas Kulmala',
    author_email = 'something@somewhere.info’,
    description = 'Project to test Jenkins CI with Python',
    install_requires = ['pandas >= 0.23.3']
)