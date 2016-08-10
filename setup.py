from setuptools import setup

with open('README.rst', 'r') as fh:
    description = '\n'.join(fh.readlines())

docs_require = [
    'sphinx>=1.4.0',
]

tests_require = [
    'pytest>=2.6.0',
    'pytest-cov>=1.7.0',
]


setup(
    name='wsgi-basic-auth',
    version='0.1.0',
    description=description,
    url='https://github.com/mvantellingen/wsgi-basic-auth',
    author="Michael van Tellingen",
    author_email="michaelvantellingen@gmail.com",
    install_requires=[
        'webob>=1.0.0',
    ],
    tests_require=tests_require,
    extras_require={
        'docs': docs_require,
        'test': tests_require,
    },
    package_dir={'': 'src'},
    py_modules=['wsgi_basic_auth'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    zip_safe=False,
)
