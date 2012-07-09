Bongo
=====

[![](https://secure.travis-ci.org/codeforamerica/bongo.png?branch=master)](http://travis-ci.org/codeforamerica/bongo)

A simple API wrapper for the [Iowa City bus data
API](http://www.ebongo.org/api/) -- mainly to use as an example for an
upcoming blog post.


Installation
------------

You can install the API wrapper using [`pip`](http://pypi.python.org/pypi/pip).

    pip install bongo


Usage
-----

There are two ways of interacting with the Bongo API.

The first way is just interacting with the `bongo` module.

```python
>>> import bongo

>>> bongo.routes()
{"routes": [1234, 5678, 9999]}

>>> bongo.route('lantern', 'coralville')
{"coralville's": {"lantern": "route"}}

>>> bongo.stops()
{"stops": [1234, 5678, 9999]}

>>> bongo.stop(8350)
{"stop": {"8350": "information"}}

>>> bongo.predict(8350)
{"stop": {"8350": "predictions"}}
```

The second way is interacting with the `Bongo` class.

```python
>>> from bongo import Bongo
>>> b = Bongo()

>>> # List of all Bongo routes.
>>> b.routes()
{"routes": [1234, 5678, 9999]}

>>> # Info for a specific route and agency.
>>> b.route('lantern', 'coralville')
{"coralville's": {"lantern": "route"}}

>>> # List of all stops.
>>> b.stops()
{"stops": [1234, 5678, 9999]}

>>> # Information for a specific stop.
>>> b.stop(8350)
{"stop": {"8350": "information"}}

>>> # Predict the arrival times at a specific stop.
>>> b.predict(8350)
{"stop": {"8350": "predictions"}}

>>> # Bongo can also be used to return XML data.
>>> Bongo('xml').routes()
<ohai><xml><data></data></xml></ohai>
```


Copyright
---------

Copyright (c) 2012 Code for America. See [LICENSE][] for details.

[license]: https://github.com/codeforamerica/bongo/blob/master/LICENSE.mkd

[![Code for America Tracker](http://stats.codeforamerica.org/codeforamerica/cfa_template.png)][tracker]

[tracker]: http://stats.codeforamerica.org/projects/bongo
