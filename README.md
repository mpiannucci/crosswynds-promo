Cosswynds-Promo
======================

Promotional micro-site for runnning a viral email compain using Python and the Google App Engine.

How it works
----------------------

To Be Written

Development
-----------------------
Created using the [web.py](https://github.com/webpy/webpy) framework for python 2.7 and the [Google App Engine](https://cloud.google.com/appengine/docs/python/gettingstartedpython27/introduction).

**Dependencies:**
* Python 2.7
* Web.py
* Google App Engine

#### Getting the Python Dependencies

Download the `web.py` Python module:

    cd myPage/
    pip install web.py -t .
    rm -r web.py-0.37.egg-info/

#### Running the Webapp

First, compile the templates used by `web.py`:

    ./compileTemplates

Then, run the development web server

    dev_appserver.py app.yaml
