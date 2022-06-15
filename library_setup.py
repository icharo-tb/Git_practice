from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Personal/Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]


setup(
    name = 'Learning Practice',
    version = '0.0.1',
    description = 'Trial enviroment',
    Long_description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url = 'https://github.com/icharo-tb',
    author = 'Daniel Lopez',
    author_email = 'daniel.lopez.pajares.2021@gmail.com',
    License = 'MIT',
    classifiers = classifiers,
    keywords = 'practice',
    packages = find_packages(),
    install_requires = ['']
)