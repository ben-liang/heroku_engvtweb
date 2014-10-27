# python-getting-started

ENGVT Cycling Web App, deployed to Heroku.

This is a stupid app with no real purpose born out of boredom and the desire to make a unnecessarily high-tech ordering system for our stupid cycling team.  But it is pretty cool.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, to deploy to Heroku you'll need to install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone git@github.com:benliang443/heroku_engvtweb.git
$ cd heroku_engvtweb
$ source activate #activates virtualenv so you don't need to install all dependencies
$ python manage.py syncdb
$ foreman start web
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ git push heroku master
$ heroku open
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

