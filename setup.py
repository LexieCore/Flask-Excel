try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

NAME = 'Flask-Excel'
AUTHOR = 'C.W.'
VERSION = '0.0.5'
EMAIL = 'wangc_2011 (at) hotmail.com'
LICENSE = 'New BSD'
PACKAGES = find_packages(exclude=['ez_setup', 'examples', 'tests'])
DESCRIPTION = (
    'A flask extension that provides one application programming interface ' +
    'to read and write data in different excel file formats' +
    ''
)
KEYWORDS = [
    'excel',
    'python',
    'pyexcel',
    'xls',
    'xlsx',
    'ods',
    'csv',
    'API',
    'Flask'
]

INSTALL_REQUIRES = [
    'pyexcel>=0.2.0',
    'pyexcel-webio>=0.0.5',
    'Flask>=0.10.1',
]

EXTRAS_REQUIRE = {
    'xls': ['pyexcel-xls>=0.1.0'],
    'xlsx': ['pyexcel-xlsx>=0.1.0'],
    'ods': ['pyexcel-ods3>=0.1.0'],
}

CLASSIFIERS = [
    'Topic :: Office/Business',
    'Topic :: Utilities',
    'Topic :: Software Development :: Libraries',
    'Programming Language :: Python',
    'License :: OSI Approved :: BSD License',
    'Intended Audience :: Developers',
    'Topic :: Internet :: WWW/HTTP',
    'Development Status :: 3 - Alpha',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Environment :: Web Environment',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Environment :: Web Environment',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries :: Python Modules'
]


def read_files(*files):
    """Read files into setup"""
    text = ""
    for single_file in files:
        text = text + read(single_file) + "\n"
    return text


def read(afile):
    """Read a file into setup"""
    with open(afile, 'r') as opened_file:
        return opened_file.read()


if __name__ == '__main__':
    setup(
        name=NAME,
        author=AUTHOR,
        version=VERSION,
        author_email=EMAIL,
        description=DESCRIPTION,
        install_requires=INSTALL_REQUIRES,
        keywords=KEYWORDS,
        extras_require=EXTRAS_REQUIRE,
        packages=PACKAGES,
        include_package_data=True,
        long_description=read_files('README.rst', 'CHANGELOG.rst'),
        zip_safe=False,
        tests_require=['nose'],
        license=LICENSE,
        classifiers=CLASSIFIERS
    )
