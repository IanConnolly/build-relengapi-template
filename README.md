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


### Relengapi Documentation

More detailed information on the Mozilla Releng API can be found in its
[repo](https://github.com/mozilla/build-relengapi) and **much** more
can be found in its [documentation](https://api.pub.build.mozilla.org/docs/).


#### TODO

* Authentication Example
* Database Example
