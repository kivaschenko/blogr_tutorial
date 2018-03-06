import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid >= 1.9',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'pyramid_retry',
    'SQLAlchemy>=1.0',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'wtforms==2.1',  # form library
    'webhelpers2==2.0', # various web building related helpers
    'paginate==0.5.6', # pagination helpers
    'paginate_sqlalchemy==0.2.0'
    ]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
]

setup(
    name='pyramid_blogr',
    version='0.0',
    description='pyramid_blogr',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = pyramid_blogr:main',
        ],
        'console_scripts': [
            'initialize_pyramid_blogr_db = pyramid_blogr.scripts.initializedb:main',
        ],
    },
)