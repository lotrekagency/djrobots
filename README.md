# Djrobots

Our internal utility to easily have robots.txt both for development and production

## Install

    pip install djrobots

## Usage

Include djrobots urls to your URLconf and your're done!

    (r'^robots\.txt$', include('djrobots.urls')),

and add djrobots to your INSTALLED_APPS

## Sitemap

If you want to specify the sitemap view in your robots.txt, provide the view name in the settings

    DJROBOTS_SITEMAP_VIEW_NAME = 'sitemap-root'

or directly an url

    DJROBOTS_SITEMAP_URL = '/sitemap-index.xml'

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
    $ ./runtests.py --with-coverage
