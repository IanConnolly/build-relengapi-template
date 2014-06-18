Mozilla Releng API Example Blueprint
===========

This is an example blueprint and project skeleton for Mozilla
Release Engineering's API. It should serve as a good starting point
for any new Releng API services.

### Installation

* Create a virtualenv and activate it.
* Install the main build-relengapi application into the virtualenv.
  (install_relengapi.sh will do this for you)
* ```export RELENGAPI_SETTINGS=$PWD/settings.py``` in the build-relengapi repository.
* ```pip install -e .``` to install the current application
* ```relengapi serve```


### Setting up authentication &amp; permissions

Some auth is simple binary, logged in-or-out logic. This is provided by the
```login_required``` decorator from ```flask.ext.login```. You can see it in use
at the ```/example/needlogin``` endpoint.

Granular access-level permissions are handled by Flask-Principal.
You can see an example of creating a permission with the ```/example/needpermission```
endpoint. To give yourself access to this endpoint you'll need to edit
```settings.py``` pointed to by ```$RELENGAPI_SETTINGS```.
The ```RELENGAPI_PERMISSIONS``` should look similar to the below:

```
RELENGAPI_PERMISSIONS = {
    'type': 'static',
    'permissions': {
        'iconnolly@mozilla.com': ['example.view.perm_example'],
    },
}
```

More documentation on authentication in Releng API blueprints can be gotten
[here]("https://api.pub.build.mozilla.org/docs/development/@relengapi/auth/").


### Relengapi Documentation

More detailed information on the Mozilla Releng API can be found in its
[repo](https://github.com/mozilla/build-relengapi) and **much** more
can be found in its [documentation](https://api.pub.build.mozilla.org/docs/).


#### TODO

* Database Example
