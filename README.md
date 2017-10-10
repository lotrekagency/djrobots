# Djrobots

Our internal utility to easily have robots.txt both for development and production

## Usage

Include djrobot urls to your URLconf and your're done!

    (r'^robots\.txt$', include('djrobots.urls')),

## Sitemap

If you want to specify the sitemap view in your robots.txt, provide the view name in the settings

    DJROBOTS_SITEMAP_VIEW_NAME = 'sitemap-root'

## Run tests

    $ pip install -r requirements-dev.txt
    $ ./runtests.py --with-coverage
