<p align="center">
<img src="https://raw.githubusercontent.com/lotrekagency/djrobots/master/logo.jpg">
<br/>
<a href="https://travis-ci.org/lotrekagency/djrobots" target="blank"><img src="https://travis-ci.org/lotrekagency/djrobots.svg?branch=master"></a>
<a href="https://pypi.python.org/pypi/djrobots/" target="blank"><img src="https://img.shields.io/pypi/v/djrobots.svg"></a>
<a href="https://codecov.io/gh/lotrekagency/djrobots" target="blank"><img src="https://codecov.io/gh/lotrekagency/djrobots/branch/master/graph/badge.svg"></a>
</p>

Our internal utility to easily have robots.txt both for development and production

## Install

    pip install djrobots

## Usage

Include djrobots urls to your URLconf and your're done!

    (r'^robots\.txt$', include('djrobots.urls')),

and add djrobots to your INSTALLED_APPS.

If you want to disable all in your website, use in your settings

    DJROBOTS_DISALLOWALL = True

## Sitemap

If you want to specify the sitemap urls in your robots.txt, provide the view name in the settings

    DJROBOTS_SITEMAPS = 'sitemap-root'

DJROBOTS_SITEMAPS is a special setting, you can use an array to specify more sitemaps in your robots.txt

    DJROBOTS_SITEMAPS = ['sitemap-root', 'department-sitemap']

or you can mix view names with raw urls

    DJROBOTS_SITEMAPS = ['sitemap-root', 'department-sitemap', '/my-sitemap-index.xml']

## Customization

By default djrobots provides a robots.txt template for production and a robots-debug.txt for development with a default configuration used internally at Lotrek.

If you want to specify more directives you can extend default templates, robots.txt and robots-debug.txt

    {% extends "djrobots/base-robots.txt" %}
    {% block content %}
    User-agent: *
    Disallow: /cgi-bin/
    Disallow: /tmp/
    Disallow: {% url 'documents' %}

    Host: example.com

    {% endblock %}

## Run tests

    $ pip install -r requirements-dev.txt
    $ make test
