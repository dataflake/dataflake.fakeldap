.. image:: https://api.travis-ci.org/dataflake/dataflake.fakeldap.svg?branch=master
   :target: https://travis-ci.org/dataflake/dataflake.fakeldap

.. image:: https://readthedocs.org/projects/dataflakefakeldap/badge/?version=latest
   :target: https://dataflakefakeldap.readthedocs.io
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/dataflake.fakeldap.svg
   :target: https://pypi.python.org/pypi/dataflake.fakeldap
   :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/dataflake.fakeldap.svg
   :target: https://pypi.python.org/pypi/dataflake.fakeldap
   :alt: Python versions

====================
 dataflake.fakeldap
====================
This package offers a mock ``python-ldap`` library that can be used 
for testing code relying on ``python-ldap`` without having to configure 
and populate a real directory server.

Starting with version 3.0 the library will behave just like ``python-ldap``
version 3.3 or higher:

- distinguished names, relative distinguished names, attribute names and
  queries are expected to be native un-encoded string values.

- attribute values are expected to be bytes values.

If you pass the wrong type of string, the library will raise a ``TypeError``.
See https://www.python-ldap.org/en/latest/bytes_mode.html for a short
description of this behavior.


Documentation
=============
Full documentation is available at
https://dataflakefakeldap.readthedocs.io/


Bug tracker
===========
A bug tracker is available at
https://github.com/dataflake/dataflake.fakeldap/issues
