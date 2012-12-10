:orphan:

Packages affiliated with the Astropy project
============================================

A major part of the Astropy project is the existence of "Affiliated
Packages". An affiliated package is an astronomy-related python package
that is not part of the `astropy` core source code, but has requested to
be included in the Astropy project. The projects are expressing an
interest in Astropy's goals of improving reuse, interoperability, and
interface standards for python astronomy and astrophysics packages.

If you are the developer of an astronomy package, and would like to become
affiliated with the Astropy project, please drop us a line on the astropy-dev
mailing list!

Python-montage
--------------

.. |mont| image:: montage.png
.. _Documentation: http://montage-wrapper.readthedocs.org/en/latest/
.. _Installation Instructions: http://montage-wrapper.readthedocs.org/en/latest/#installation

+--------+-------------------------------------------------------------------+
| |mont| | **About:** Montage-wrapper is a pure Python module that provides a|
|        | Python API to the Montage Astronomical Image Mosaic Engine,       |
|        | including both functions to access individual Montage commands,   |
|        | and high-level functions to facilitate mosaicking and             |
|        | re-projecting. Python-montage uses the Astropy core package for   |
|        | reading and writing FITS files.                                   |
|        |                                                                   |
|        | **Developer:** Thomas Robitaille                                  |
|        |                                                                   |
|        | `Documentation`_ - `Installation Instructions`_                   |
|        |                                                                   |
+--------+-------------------------------------------------------------------+

In development
--------------

A few additional affiliated packages are currently in development, including:

* `photutils <http://photutils.readthedocs.org/en/latest/>`_: photometry tools
* `astroquery <http://astroquery.readthedocs.org/en/latest/>`_: online database querying
* `specutils <https://github.com/astropy/specutils>`_: spectroscopic analysis utilities
* `pyidlastro <https://github.com/astropy/pyidlastro>`_: straight port of IDL routines
* `kcorrect <https://github.com/astropy/kcorrect>`_: Python bindings to kcorrect code of Blanton et al. 2007

These packages are still very much in development, and the user interface (API) may not be stable. If you do try these packages, please do report any issues to the developers, so 

Registry
--------

To see the full list of registered affiliated packags, or for information on
registering your package, see the :ref:`registry`.
