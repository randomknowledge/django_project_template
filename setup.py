# coding=utf-8
from setuptools import setup
import finddata


setup(
    name="{{ project_name }}",
    author="Florian Finke",
    author_email="flo@randomknowledge.org",
    version='0.0.1',
    packages=['{{ project_name }}'],
    package_data=finddata.find_package_data(),
    url='https://github.com/randomknowledge/{{ project_name }}',
    include_package_data=True,
    license='MIT',
    description='',
    long_description=open('Readme.md').read(),
    zip_safe=False,
    install_requires=['Django==1.5.4', 'South==0.8.2', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
