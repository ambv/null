----
null
----

Implements the `null object pattern
<http://en.wikipedia.org/wiki/Null_Object_pattern>`_.

Provides:

- a ``Null`` singleton that can be used like ``None`` (but is not ``None`` and
  is not equal to ``None``)
  
- a ``NullList`` that returns ``Null`` instead of raising ``IndexError``
  
- a ``NullDict`` that returns ``Null`` instead of raising ``KeyError``
  
- a ``nullify()`` routine that converts mappings and sequences to the nullified
  variant

- an ``unset`` singleton for clearing up APIs to distinguish between a keyword
  argument that is set by the user as ``None`` and simply not set by the user

How do I run the tests?
-----------------------

The easiest way would be to extract the source tarball and run::

  $ python test/test_null.py

Change Log
==========

0.6.1
-----

* ``MANIFEST.in`` will forever be my favourite gotcha of Python packaging

* PEP8-fied the sources

0.6.0
-----

* long overdue Python 3 support

0.5.0
-----

* initial published version

Authors
=======

Glued together by `Łukasz Langa <mailto:lukasz@langa.pl>`_.
