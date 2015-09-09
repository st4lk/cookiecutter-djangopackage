#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import {{ cookiecutter.app_name }}

from setuptools import setup, find_packages

version = {{ cookiecutter.app_name }}.__version__

def __read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'generate_rst':
    os.system('pandoc --from=markdown --to=rst --output=README.rst README.md')
    os.system('pandoc --from=markdown --to=rst --output=HISTORY.rst HISTORY.md')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = __read('README.rst'),
history = __read('HISTORY.rst'),
install_requires = __read('requirements.txt').split()

setup(
    name='{{ cookiecutter.project_name }}',
    version=version,
    description="""{{ cookiecutter.project_short_description }}""",
    long_description=readme + '\n\n' + history,
    platforms=('Any'),
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    license="BSD",
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],
)
