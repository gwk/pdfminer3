from setuptools import setup
import sys

import pdfminer3 as package

requires = ['pycryptodome', 'sortedcontainers']
if sys.version_info >= (3, 0):
    requires.append('chardet')

setup(
    name='pdfminer3',
    version=package.__version__,
    packages=['pdfminer3'],
    package_data={'pdfminer3': ['cmap/*.pickle.gz']},
    install_requires=requires,
    description='PDF parser and analyzer',
    long_description=package.__doc__,
    license='MIT/X',
    author='Yusuke Shinyama & contributors',
    author_email='george.w.king@gmail.com',
    url='https://github.com/gwk/pdfminer3',
    scripts=[
        'tools/pdf2txt.py',
        'tools/dumppdf.py',
        'tools/latin2ascii.py',
    ],
    keywords=[
        'pdf',
        'pdf parser',
        'pdf converter',
        'layout analysis',
        'text mining',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Text Processing',
    ],
)
