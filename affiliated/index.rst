:orphan:

About affiliated packages
=========================

A major part of the Astropy project is the existence of "Affiliated
Packages". An affiliated package is an astronomy-related Python package
that is not part of the astropy core package, but has requested to
be included in the Astropy project. These packages are expressing an
interest in Astropy's goals of improving reuse, interoperability, and
interface standards for python astronomy and astrophysics packages.

If you are the developer of an astronomy package, and would like to become
affiliated with the Astropy project, please drop us a line on the `astropy-dev <http://groups.google.com/group/astropy-dev>`_ mailing list!

Featured packages
=================

Montage-wrapper
---------------

.. |mont| image:: montage.png

.. |monthome| replace:: Home
.. _monthome: http://www.astropy.org/montage-wrapper

.. |montdocs| replace:: Documentation
.. _montdocs: http://montage-wrapper.readthedocs.org/

.. |montinst| replace:: Installation
.. _montinst: http://montage-wrapper.readthedocs.org/en/latest/#installation

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
|        | |monthome|_ - |montdocs|_ - |montinst|_                           |
|        |                                                                   |
+--------+-------------------------------------------------------------------+

Ginga
-----

.. |ginga| image:: ginga.png

.. |gingahome| replace:: Home and Installation
.. _gingahome: http://ejeschke.github.io/ginga/

+--------+-------------------------------------------------------------------+
||ginga| | **About:** Ginga is a viewer for astronomical data FITS (Flexible |
|        | Image Transport System) files. The Ginga viewer centers around a  |
|        | new FITS display widget which supports zooming and panning, color |
|        | and intensity mapping, a choice of several automatic cut levels   |
|        | algorithms and canvases for plotting scalable geometric forms.    |
|        |                                                                   |
|        | **Developer:** Eric Jeschkee                                      |
|        |                                                                   |
|        | |gingahome|_                                                      |
|        |                                                                   |
+--------+-------------------------------------------------------------------+


APLpy
-----

.. |aplpy| image:: aplpy.png

.. |aplpyhome| replace:: Home
.. _aplpyhome: http://aplpy.github.io

.. |aplpydocs| replace:: Documentation
.. _aplpydocs: http://aplpy.readthedocs.org

.. |aplpyinst| replace:: Installation
.. _aplpyinst: http://aplpy.github.io/install.html

+--------+-------------------------------------------------------------------+
||aplpy| | **About:** APLpy (the Astronomical Plotting Library in Python) is |
|        | a Python module aimed at producing publication-quality plots of   |
|        | astronomical imaging data in FITS format. The module uses         |
|        | Matplotlib, a powerful and interactive plotting package. It is    |
|        | capable of creating output files in several graphical formats,    |
|        | including EPS, PDF, PS, PNG, and SVG.                             |
|        |                                                                   |
|        | **Developers:** Thomas Robitaille, Eli Bressert, Adam Ginsburg    |
|        |                                                                   |
|        | |aplpyhome|_ - |aplpydocs|_ - |aplpyinst|_                        |
|        |                                                                   |
+--------+-------------------------------------------------------------------+

Other packages
==============

Stable packages
---------------

* `astroML <http://astroml.github.com/>`_: tools for machine learning and data mining in Astronomy
* `Astropysics <http://packages.python.org/Astropysics/>`_: library of IDL astronomy routines converted to Python.

In development
--------------

A few additional affiliated packages are currently in development, including:

* `photutils <http://photutils.readthedocs.org/en/latest/>`_: photometry tools
* `astroquery <http://astroquery.readthedocs.org/en/latest/>`_: online database querying
* `specutils <https://github.com/astropy/specutils>`_: spectroscopic analysis utilities
* `kcorrect <https://github.com/astropy/kcorrect>`_: Python bindings to kcorrect code of Blanton et al. 2007

These packages are still very much in development, and the user interface (API) may not be stable. If you do try these packages, please do report any issues to the developers, so 

Affiliated Package Registry
===========================

The following table below lists all currently registered affiliated packages.
This table is determined from the http://affiliated.astropy.org/registry.json
file that contains the actual registry. The *Stable* column indicates whether
the package maintainer consider the package to be ready for use. Packages that
are under heavy development and for which the user interface is likely to
change significantly in the near future are marked as *No*.

.. The javascript at the bottom does the actual table populating

+--------------+---------+-----------+----------+-----------------+------------+
| Package Name | Stable  | PyPI Name | Web Page | Code Repository | Maintainer |
+==============+=========+===========+==========+=================+============+
| Loading...   |         +           +          +                 |            |
+--------------+---------+-----------+----------+-----------------+------------+

.. raw:: html

    <script type="text/javascript">

    //Using jQuery is ok because it is needed by and bundled with sphinx

    //Quirk to note: the jQuery.getJSON function fails if you open this locally
    //with Chrome, because Chrome thinks local JSON files are unsafe for some
    //reason.  Use basically any other modern browser, or it works fine if its
    //actually on the web server even with chrome.

    function url_translator(urltext) {
        if (urltext == undefined) {
            return 'None';
        } else {
            return '<a href="' + urltext + '">' + urltext + '</a>';
        }
    }

    function pypi_translator(pypiname) {
        if (pypiname == undefined) {
            return 'None';
        } else {
            var urltext = 'http://pypi.python.org/pypi/' + pypiname;
            return '<a href="' + urltext + '">' + pypiname + '</a>';
        }
    }

    function stable_translator(stable) {
        if (stable) {
            return 'Yes';
        } else {
            return 'No';
        }
    }

    var _email_regex_str = '[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}';
    var _email_regex  = new RegExp(_email_regex_str, 'i');
    var _email_with_name_regex  = new RegExp('(.+)<(' + _email_regex_str + ')>', 'i');

    function maintainer_translator(maint, pkgnm) {
        var url, match;
        if (_email_with_name_regex.test(maint)) {
            match = _email_with_name_regex.exec(maint);
            url = 'mailto:' + match[2] + '?subject=Astropy%20affiliated%20package%20' + pkgnm;
            return '<a href="' + url + '">' + match[1] + '</a>';
        } else if (_email_regex.test(maint)) {
            url = 'mailto:' + maint + '?subject=Astropy%20affiliated%20package%20' + pkgnm;
            return '<a href="' + url + '">' + maint + '</a>';
        } else {
            return maint;
        }
    }

    function populateTable(data, tstat, xhr) {
        var tab = document.getElementsByTagName('table')[0];
        tab.deleteRow(1);
        var ncols = tab.rows[0].cells.length;

        var pkgi, row, nmcell, stablecell, pypicell, urlcell, rpocell, maintcell;
        if (data == null) {
            row = tab.insertRow(1);
            row.insertCell(0).innerHTML = 'Could not load registry file!';
            for (i=0;i<(ncols - 1);i++) {
                row.insertCell(i + 1).innerHTML = ' ';
            }
        } else {
            var pkgs = data.packages;
            
            //First figure out the correct order if we sort on the name
            var nmarr = new Array(pkgs.length)
            var sortorder = new Array(pkgs.length)
            for (i=0; i<pkgs.length; i++) {
                pkgi = pkgs[i];
                nmarr[i] = pkgi.name;
                sortorder[i] = i;
            }
            // This "sorts" the indecies using a compare function that actually sorts nmarr
            sortorder.sort(function (a, b) { return nmarr[a] < nmarr[b] ? -1 : nmarr[a] > nmarr[b] ? 1 : 0; });
            
            for (i=0; i<sortorder.length; i++) {
                pkgi = pkgs[sortorder[i]];
                row = tab.insertRow(i + 1);

                nmcell = row.insertCell(0);
                stablecell = row.insertCell(1);
                pypicell = row.insertCell(2);
                urlcell = row.insertCell(3);
                repocell = row.insertCell(4);
                maintcell = row.insertCell(5);

                nmcell.innerHTML = pkgi.name;
                stablecell.innerHTML = stable_translator(pkgi.stable);
                pypicell.innerHTML = pypi_translator(pkgi.pypi_name);
                urlcell.innerHTML = url_translator(pkgi.home_url);
                repocell.innerHTML = url_translator(pkgi.repo_url);
                maintcell.innerHTML = maintainer_translator(pkgi.maintainer, pkgi.name);
            }
        }
    }

    // Make sure the doc is loaded before doing anything
    $(document).ready(function() {
        $.getJSON("registry.json", populateTable);
    });

    </script>

To include your python astronomy package in this registry, contact the
coordination committee by e-mailing `astropy.team@gmail.com
<mailto:astropy.team@gmail.com?subject=Affiliated%20package%20registration%20request%20for%20YOURPKGNAMEHERE>`_.

