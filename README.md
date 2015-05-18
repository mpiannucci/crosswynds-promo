Cosswynds-Promo
======================

Promotional micro-site for runnning a viral email compain using Python and the Google App Engine. This web app is modeled after the article found [here](http://fourhourworkweek.com/2014/07/21/harrys-prelaunchr-email/) about Harry's Prelaunch campaign. 

How it works
----------------------

The original web app was written with Ruby on Rails, which I do not know. I decided to port it to python, and in an effort to keep the cost free to the client, the Google App Engine. It works very similar to the original app. It prompts a simple signup page, which leads to referral site where the user may claim a unique referral link to share with friends. The amount of user that sign up using each referral link is logged, and the more referrals, the more rewards. the user also recieves an email upon sign up so they have a copy of both the unique referral link, and the place to track their referrals. 

The main motivation for this project is email harvesting to create a mailing list. That mailing list is crucial when a new online product or site is being launched and you need to get the word out when youre ready to sell. 

Modifying It for Your Company/Cause/Product
-----------------------
This site can be quickly modified for your own use. However it takes some technical knowledge, specifically of CSS, HTML. Python knowledge isn't necessary but it certaintly wouldn't hurt. Below are the general steps that need to be followed to produce your own version of the webapp. 

1. Using your Google account (or make one if you don't have one), login to http://console.developers.google.com . You need to create a new project with whatever name you want to deploy to. 
2. Get the dependencies described below by the "Developers" section of this document. 
3. Modify the HTML and images to match your brand. All of the images and HTML included are targeted for Crosswynds Traders. You will need to work to make these look like they are specifically for your own target.
4. Follow the Development instructions to compile your HTML files and test the program locally. If you like what you see and you're ready to launch, follow the instructions to deploy your app. 
5. SHARE with anyone and everyone to maximize feedback (NOTE: If your product is REAAALLLYY popular, you may have to [request increase mail usage](https://cloud.google.com/appengine/docs/quotas#Mail).
6. When your promotion is over, be sure to disable the application. 

Development
-----------------------
Created using the [web.py](https://github.com/webpy/webpy) framework for python 2.7 and the [Google App Engine](https://cloud.google.com/appengine/docs/python/gettingstartedpython27/introduction).

**Dependencies:**
* Python 2.7
* Web.py
* Google App Engine

#### Getting the Python Dependencies

Download the `web.py` Python module:

    cd crosswynds-promo/
    pip install web.py -t .
    rm -r web.py-0.37.egg-info/

#### Running the Webapp

First, compile the templates used by `web.py`:

    ./compileTemplates

Then, run the development web server

    dev_appserver.py app.yaml

License
-----------------------
Licensed under the [MIT License](LICENSE).
