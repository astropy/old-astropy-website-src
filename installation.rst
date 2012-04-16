Installation
============

.. _`documentation`: http://astropy.readthedocs.org/en/latest/install.html
.. _`issue tracker`: http://github.com/astropy/astropy/issues
.. _`astropy-users`: http://groups.google.com/group/astropy-users
.. _`Numpy`: http://numpy.scipy.org
.. _`Python`: http://www.python.org

Detailed installation instructions are provided in the `documentation`_, but
we have included a simplified version here.

Astropy requires `Python`_ 2.6, 2.7, 3.1, or 3.2, and `Numpy`_ 1.4.0 or later.

Install from Source
-------------------

At the moment, you can install the latest developer version of Astropy using::

    git clone http://github.com/astropy/astropy.git
    cd astropy
    python setup.py install

If you do not have git installed, you can instead of to the `downloads <https://github.com/astropy/astropy/downloads>`_ page, and click on 'Download as tar.gz', then expand the resulting tar file, go into the directory, and type::

    python setup.py install

Note that once a stable version of Astropy is released, it will be possible to
install Astropy using::

    pip install astropy

Testing your installation
-------------------------

You can check that astropy is correctly installed by starting up ``python`` or ``ipython``, and importing ``astropy``::

    >>> import astropy
    >>> astropy.test()

If you do not get any errors, the installation was successful! If you have issues getting Astropy installed, either post a message to the `astropy-users`_ mailing list, or report the issue on our `issue tracker`_!

Package managers
----------------

Once a stable version of Astropy is released, it will be possible to install
Astropy using various package managers (MacPorts, Fink, etc.). This section
will be updated to reflect the different package managers that are available.
