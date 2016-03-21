# ENGVTWeb

ENGVT Cycling Web App, deployed to Heroku.

This is a stupid app with no real purpose born out of boredom and the desire to make a unnecessarily high-tech ordering system for our stupid cycling team.  But it is pretty cool.

# Running Locally

### Mac OSX Machine & VENV Setup

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, to deploy to Heroku you'll need to install the [Heroku Toolbelt](https://toolbelt.heroku.com/).  Also, assuming you're using a Mac, you'll need to install [Homebrew](http://brew.sh/) to install system dependencies needed to run the app locally. If you're not using a Mac, that blows.

```sh
$ git clone git@github.com:benliang443/heroku_engvtweb.git
$ cd heroku_engvtweb
$ ./setup_homebrew.sh             # installs system dependencies with homebrew
$ virtualenv venv                 # creates local python virtual environment
$ source activate                 # activates virtualenv
$ pip install -r requirements.txt # installs python packages to ./venv
$ pip install gunicorn            # needed to run local WSGI server
```

### Heroku Setup

Heroku uses environment variables for EVERYTHING, and as of right now this app is far too useless to care enough to set up proper local, staging & production environments.  So what that means is that there is only one environment: PRODUCTION. 
So to run locally, you'll need to clone all Heroku production environment variables to your local `.env` file.

Assuming you've already installed [Heroku Toolbelt](https://toolbelt.heroku.com/), run the following from your project directory:

```sh
$ heroku login                              # need to log in first
$ heroku config -s --app engvtweb >> .env   # saves ALL production config variables to your local .env file
```

### Running the App

```sh
$ python manage.py syncdb 
$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ git push heroku master
$ heroku open
```

# Updating @^# Catalog
Updating the @^# catalog is done on a one-off basis as needed.  Doing so will destroy all exiting items in the catalog,
 thereby killing all foreign-key refs from previous orders. This really shouldn't matter very much

```
$ heroku run bash --app engvtweb #run bash shell in a one-off dyno
$ curl "[the catalog url]" > qbpcatalog-ascii.txt
$ iconv -f ASCII -t utf-8//IGNORE qbpcatalog-ascii.txt > qbpcatalog.txt # force re-encode the catalog to UTF-8
$ python manage.py import_new_qbp_catalog # runs management command to destroy existing catalog & import new one from TSV file
$ python manage.py rebuild_index # rebuilds the search index
```




## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

