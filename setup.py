import codecs
import os
from setuptools import setup, find_packages


def read(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    return codecs.open(filepath, encoding='utf-8').read()


setup(
    name='lemon-robots',
    version='0.1.dev',
    license='BSD',
    description='robots.txt simple app for Django',
    long_description=read('README.rst'),
    author='Mike Yumatov',
    author_email='mike@yumatov.org',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
