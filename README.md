pdfminer3
============

gwk/pdfminer3 is a Python 3.7 fork of pdfminer/pdfminer.six.
It was forked in December of 2018 to experiment with a Python 3 version of the library.
Since then the original has migrated to Python 3 only and this fork is now very stale.
However there might be a few small fixes here that could still be applicable to the community version.

This fork is kept for archive purposes only.

pdfminer3 is a tool for extracting information from PDF documents.
Unlike other PDF-related tools, it focuses entirely on getting
and analyzing text data. pdfminer3 allows one to obtain
the exact location of text in a page, as well as
other information such as fonts or lines.
It includes a PDF converter that can transform PDF files
into other text formats (such as HTML). It has an extensible
PDF parser that can be used for other purposes than text analysis.

 * Webpage: https://github.com/gwk/pdfminer3/
 * Download (PyPI): https://pypi.python.org/pypi/pdfminer3/


Features
--------

 * Written entirely in Python.
 * Parse, analyze, and convert PDF documents.
 * PDF-1.7 specification support. (well, almost)
 * CJK languages and vertical writing scripts support.
 * Various font types (Type1, TrueType, Type3, and CID) support.
 * Basic encryption (RC4) support.
 * Outline (TOC) extraction.
 * Tagged contents extraction.
 * Automatic layout analysis.


How to Install
--------------

 * Install Python 2.7 or newer. (Python 3.x is supported in pdfminer3)
 * Install

    `pip install pdfminer3`

 * Run the following test:

    `pdf2txt.py samples/simple1.pdf`


Command Line Tools
------------------

pdfminer3 comes with two handy tools:
pdf2txt.py and dumppdf.py.

**pdf2txt.py**

pdf2txt.py extracts text contents from a PDF file.
It extracts all the text that are to be rendered programmatically,
i.e. text represented as ASCII or Unicode strings.
It cannot recognize text drawn as images that would require optical character recognition.
It also extracts the corresponding locations, font names, font sizes, writing
direction (horizontal or vertical) for each text portion.
You need to provide a password for protected PDF documents when its access is restricted.
You cannot extract any text from a PDF document which does not have extraction permission.

(For details, refer to /docs/index.html.)

**dumppdf.py**

dumppdf.py dumps the internal contents of a PDF file in pseudo-XML format.
This program is primarily for debugging purposes,
but it's also possible to extract some meaningful contents (e.g. images).

(For details, refer to /docs/index.html.)


TODO
----

 * PEP-8 and PEP-257 conformance.
 * Better documentation.
 * Performance improvements.


Terms and Conditions
--------------------

(This is so-called MIT/X License)

Copyright (c) 2004-2014  Yusuke Shinyama <yusuke at cs dot nyu dot edu>

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
