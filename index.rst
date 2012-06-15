.. title:: Welcome

.. _`PyFITS`: http://www.stsci.edu/institute/software_hardware/pyfits
.. _`PyWCS`: https://trac.assembla.com/astrolib
.. _`vo`: https://trac.assembla.com/astrolib
.. _`asciitable`: http://cxc.harvard.edu/contrib/asciitable/
.. _`astropy`: http://mail.scipy.org/mailman/listinfo/astropy
.. _`astropy-dev`: http://groups.google.com/group/astropy-dev
.. _`issue tracker`: http://github.com/astropy/astropy/issues
.. _`documentation`: http://astropy.readthedocs.org/en/latest/install.html
.. _`Numpy`: http://numpy.scipy.org
.. _`Python`: http://www.python.org

.. raw:: html

    <div class='logo_banner'>

.. image:: logos/astropy_banner_96.png

.. raw:: html

    </div>

The Astropy project is a common effort to develop a single core package for
Astronomy that brings together almost 100 developers from around the world.

Development is actively ongoing, with major packages such as `PyFITS`_,
`PyWCS`_, `vo`_, and `asciitable`_ already merged in, and many more components
being worked on. In particular, we are developing imaging, photometric, and
spectroscopic functionality, as well as frameworks for cosmology, unit
handling, and coordinate transformations

Stay updated by following `@astropy <http://twitter.com/#!/astropy>`_ on Twitter, or sign up to the `astropy`_ mailing list!  

If you want to get involved in Astropy development efforts, or other 
more technical discussions of Astropy, join the `astropy-dev`_ list.

If you are interested in a detailed description of the plan for the Astropy project, you can read the :doc:`original vision <vision>` for the package.

Documentation
-------------

The documentation for the `astropy` core package is available at the
websites listed below. The first is for the most recent released
version.  The second is for a version of the documentation that is 
automatically updated any time a change is made to the 
`astropy source code repository <http://github.com/astropy/astropy>`_.

* `Stable version (docs.astropy.org) <http://docs.astropy.org>`_
* `Latest developer version <http://docs.astropy.org/en/latest/index.html>`_ 
    


Installing
----------

Detailed installation instructions are provided in the `documentation`_, but
we have included a simplified version here.

Astropy requires `Python`_ 2.6, 2.7, 3.1, or 3.2, and `Numpy`_ 1.4 or later.
You can install the latest developer version of Astropy using::

    git clone http://github.com/astropy/astropy.git
    cd astropy
    python setup.py install

Once a stable version of Astropy is released, we will provide links to the tar file, and updated installation instructions!

You can check that astropy is correctly installed by starting up ``python`` or ``ipython``, and importing ``astropy``::

    >>> import astropy

If you do not get any errors, the installation was successful!

Getting help
------------

If you want to discuss issues with other Astropy users, you can sign up
to the `astropy`_ mailing list.  Alternatively, the `astropy-dev`_ list
is where you should go to discuss more technical aspects of Astropy.

Reporting issues
----------------

If you have come across something that you believe is a bug, please open a
ticket in the Astropy `issue tracker`_, and we will look into it promptly!

