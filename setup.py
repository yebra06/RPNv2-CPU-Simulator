import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='RPNv2 CPU Simulator',
    version='2',
    url='',
    license='BSD3',
    author='Alfredo Yebra Jr.',
    author_email='fred.yebra@gmail.com',
    description='Python CPU emulator Single Cycle CPU virtual machine',
    long_description=read('README.rst'),
    packages=['src'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_required=(
        'nose>=1.3.7'
        ),
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers :: Employers',
        'License :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Postfix :: Stack :: CPU :: Software Development :: Libraries :: Python Modules'
    ]
)
