"""
Setup and installation for the package.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="bongo",
    version="0.2",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    description="An API wrapper for Iowa City's bus data",
    long_description=open('README.md').read(),
    packages=[
        'bongo'
    ],
    install_requires=[
        'mock',
        'simplejson',
        'requests',
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
