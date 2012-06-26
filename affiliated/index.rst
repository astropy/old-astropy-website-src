:orphan:

Astropy Affilated Package Registry
----------------------------------

Description of apkg's here

Registering Packages
^^^^^^^^^^^^^^^^^^^^

Give instructions here for registering


Currently Registered Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. The javascript at the bottom does the actual table populating

+--------------+---------+-----------+----------+-----------------+------------+
| Package Name | Stable? | PyPI Name | Web Page | Code Repository | Maintainer |
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


    function populateTable(data, tstat, xhr) {
        var tab = document.getElementsByTagName('table')[0];
        tab.deleteRow(1);

        var pkgi, row, nmcell, stablecell, pypicell, urlcell, rpocell, maintcell;
        var pkgs = data.packages;
        for (i=0; i<pkgs.length; i++) {
            pkgi = pkgs[i]
            row = tab.insertRow(i + 1);

            nmcell = row.insertCell(0);
            stablecell = row.insertCell(1);
            pypicell = row.insertCell(2);
            urlcell = row.insertCell(3);
            repocell = row.insertCell(4);
            maintcell = row.insertCell(5);

            nmcell.innerHTML = pkgi.name;
            stablecell.innerHTML = pkgi.stable;
            pypicell.innerHTML = pkgi.pypi_name;
            urlcell.innerHTML = pkgi.home_url;
            repocell.innerHTML = pkgi.repo_url;
            maintcell.innerHTML = pkgi.maintainer;
        }
    }

    // Make sure the doc is loaded before doing anything
    $(document).ready(function() {
        $.getJSON("registry.json", populateTable);
    });

    </script>
