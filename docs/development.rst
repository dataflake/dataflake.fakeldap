=============
 Development
=============


Getting the source code
=======================
The source code is maintained on GitHub. To check out the trunk:

.. code-block:: sh

  $ git clone https://github.com/dataflake/dataflake.fakeldap.git

You can also browse the code online at
https://github.com/dataflake/dataflake.fakeldap


Bug tracker
===========
For bug reports, suggestions or questions please use the 
GitHub issue tracker at
https://github.com/dataflake/dataflake.fakeldap/issues.


Running the tests in a ``virtualenv``
=====================================
If you use the ``virtualenv`` package to create lightweight Python
development environments, you can run the tests using nothing more
than the ``python`` binary in a virtualenv.  First, create a scratch
environment:

.. code-block:: sh

   $ /path/to/virtualenv --no-site-packages /tmp/virtualpy

Next, get this package registered as a "development egg" in the
environment:

.. code-block:: sh

   $ /tmp/virtualpy/bin/python setup.py develop

Finally, run the tests using the build-in ``setuptools`` testrunner:

.. code-block:: sh

   $ /tmp/virtualpy/bin/python setup.py test
   running test
   ...
   test_search_startswithendswith_wildcard (dataflake.fakeldap.tests.test_fakeldap_search.FakeLDAPSearchTests) ... ok
   
   ----------------------------------------------------------------------
   Ran 56 tests in 0.033
   
   OK

If you have the :mod:`nose` package installed in the virtualenv, you can
use its testrunner too:

.. code-block:: sh

   $ /tmp/virtualpy/bin/easy_install nose
   ...
   $ /tmp/virtualpy/bin/python setup.py nosetests
   running nosetests
   ....................................................
   ----------------------------------------------------------------------
   Ran 57 tests in 0.049s

   OK

or:

.. code-block:: sh

   $ /tmp/virtualpy/bin/nosetests
   .....................................................
   ----------------------------------------------------------------------
   Ran 63 tests in 0.072s

   OK

If you have the :mod:`coverage` package installed in the virtualenv,
you can see how well the tests cover the code:

.. code-block:: sh

   $ /tmp/virtualpy/bin/easy_install nose coverage
   ...
   $ /tmp/virtualpy/bin/python setup.py nosetests \
       --with-coverage --cover-package=dataflake.fakeldap
   running nosetests
   ...
   .........................................................
   Name                 Stmts   Miss  Cover   Missing
   --------------------------------------------------
   dataflake.fakeldap     397     45    89%   ...
   ----------------------------------------------------------------------
   Ran 57 tests in 0.071s

   OK


Running the tests using  :mod:`zc.buildout`
===========================================
:mod:`dataflake.fakeldap` ships with its own :file:`buildout.cfg` file and
:file:`bootstrap.py` for setting up a development buildout:

.. code-block:: sh

  $ python bootstrap.py
  ...
  Generated script '.../bin/buildout'
  $ bin/buildout
  ...

Once you have a buildout, the tests can be run as follows:

.. code-block:: sh

   $ bin/test 
   Running tests at level 1
   Running zope.testrunner.layer.UnitTests tests:
     Set up zope.testrunner.layer.UnitTests in 0.000 seconds.
     Running:
   ..............................................................
     Ran 62 tests with 0 failures and 0 errors in 0.043 seconds.
   Tearing down left over layers:
     Tear down zope.testrunner.layer.UnitTests in 0.000 seconds.


Building the documentation using :mod:`zc.buildout`
===================================================
The :mod:`dataflake.fakeldap` buildout installs the Sphinx 
scripts required to build the documentation, including testing 
its code snippets:

.. code-block:: sh

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

.. code-block:: sh

  $ bin/buildout -o
  $ python setup.py sdist bdist_wheel upload --sign

The ``bin/buildout`` step will make sure the correct package information 
is used.
