.. image:: https://raw.githubusercontent.com/lotrekagency/djrobots/master/logo.jpg
   :target: https://raw.githubusercontent.com/lotrekagency/djrobots/master/logo.jpg
   :alt: Logo




.. image:: https://travis-ci.org/lotrekagency/djrobots.svg?branch=master
   :target: https://travis-ci.org/lotrekagency/djrobots
   :alt: Build Status

.. image:: https://codecov.io/gh/lotrekagency/djrobots/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/lotrekagency/djrobots
   :alt: codecov


.. image:: https://img.shields.io/pypi/v/djrobots.svg
   :target: https://pypi.python.org/pypi/djrobots/
   :alt: Latest Version


Our internal utility to easily have robots.txt both for development and production

-------
Install
-------

.. code-block::

   pip install djrobots

-----
Usage
-----

Include djrobots urls to your URLconf and your're done!

.. code-block::

   (r'^robots\.txt$', include('djrobots.urls')),


and add djrobots to your INSTALLED_APPS.

If you want to disable all in your site, use in your settings

.. code-block::

   DJROBOTS_DISALLOWALL = True


-------
Sitemap
-------

If you want to specify the sitemap urls in your robots.txt, provide the view name in the settings

.. code-block::

   DJROBOTS_SITEMAPS = 'sitemap-root'


DJROBOTS_SITEMAPS is a special setting, you can use an array to specify more sitemaps in your robots.txt

.. code-block::

   DJROBOTS_SITEMAPS = ['sitemap-root', 'department-sitemap']


or you can mix view names with raw urls

.. code-block::

   DJROBOTS_SITEMAPS = ['sitemap-root', 'department-sitemap', '/my-sitemap-index.xml']


-------------
Customization
-------------

By default djrobots provides a robots.txt template for production and a robots-debug.txt for development with a default configuration used internally at Lotrek.

If you want to specify more directives you can extend default templates, robots.txt and robots-debug.txt

.. code-block::

   {% extends "djrobots/base-robots.txt" %}
   {% block content %}
   User-agent: *
   Disallow: /cgi-bin/
   Disallow: /tmp/
   Disallow: {% url 'documents' %}

   Host: example.com

   {% endblock %}

---------
Run tests
---------

.. code-block::

   $ pip install -r requirements-dev.txt
   $ make test
