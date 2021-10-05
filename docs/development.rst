=============
 Development
=============


Getting the source code
=======================
The source code is maintained on GitHub. To check out the trunk:

.. code-block:: console

  $ git clone https://github.com/dataflake/dataflake.fakeldap.git

You can also browse the code online at
https://github.com/dataflake/dataflake.fakeldap


Bug tracker
===========
For bug reports, suggestions or questions please use the 
GitHub issue tracker at
https://github.com/dataflake/dataflake.fakeldap/issues.


Running the tests
=================

.. note::
    The module now uses :mod:`volatildap` to do comparison tests between
    this module and a live LDAP server. In order for this to work you must have
    a ``slapd`` and ``slaptest`` binary for OpenLDAP version 2.4 in the search
    path.

:mod:`dataflake.fakeldap` ships with its own :file:`buildout.cfg` buildout
configuration file. The buildout procedure will set up all requirements
for running the unit tests and building the documentation.

.. code-block:: console

    $ cd dataflake.fakeldap
    $ python2.7 -m virtualenv .     # PYTHON 2
    $ python3 -m venv .             # PYTHON 3
    $ bin/pip install -U pip        # Make sure pip is compatible
    $ bin/pip install zc.buildout
    $ bin/buildout
    ...

Once you have a buildout, the tests can be run as follows:

.. code-block:: console

   $ bin/test 
   Running tests at level 1
   Running zope.testrunner.layer.UnitTests tests:
     Set up zope.testrunner.layer.UnitTests in 0.000 seconds.
     Running:
   ..............................................................
     Ran 62 tests with 0 failures and 0 errors in 0.043 seconds.
   Tearing down left over layers:
     Tear down zope.testrunner.layer.UnitTests in 0.000 seconds.


The package also ships with a ``tox`` configuration that will run the tests
across all supported Python versons, and the linting and code coverage check:

.. code-block:: console

    $ bin/tox
    ...
    py27: commands succeeded
    py34: commands succeeded
    py35: commands succeeded
    py36: commands succeeded
    py37: commands succeeded
    py38: commands succeeded
    pypy: commands succeeded
    pypy3: commands succeeded
    coverage: commands succeeded
    flake8: commands succeeded


Building the documentation using :mod:`zc.buildout`
===================================================
The :mod:`dataflake.fakeldap` buildout installs the Sphinx 
scripts required to build the documentation, including testing 
its code snippets:

.. code-block:: console

    $ cd docs
    $ make html
    ...
    build succeeded.

    Build finished. The HTML pages are in _build/html.


Making a release
================
These instructions assume that you have a development sandbox set 
up using :mod:`zc.buildout` as the scripts used here are generated 
by the buildout.

.. code-block:: console

    $ cd dataflake.fakeldap
    $ bin/pip install -U wheel twine
    $ rm -rf dist
    $ bin/buildout -N
    $ bin/buildout setup setup.py sdist bdist_wheel
    $ bin/twine upload -s dist/*

The ``bin/buildout`` step will make sure the correct package information 
is used.
