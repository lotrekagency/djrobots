# Djrobots

Our internal utility to easily have robots.txt both for development and production

## Usage

Include djrobot urls to your URLconf and your're done!

    (r'^robots\.txt$', include('djrobots.urls')),

## Run tests

    $ pip install -r requirements-dev.txt
    $ ./runtests.py --with-coverage