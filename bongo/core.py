"""
A simple wrapper for the Bongo Iowa City bus API.
"""

import requests as req
import simplejson as json


class Bongo(object):
    """
    A simple Python wrapper for the Bongo Iowa City bus API.
    """

    def __init__(self, format='json'):
        self.format = format

    def get(self, endpoint, **kwargs):
        """Perform a HTTP GET request to the API and return the data."""
        if 'format' not in kwargs:
            kwargs['format'] = self.format
        url = "http://ebongo.org/api/%s" % (endpoint)
        request = req.get(url, params=kwargs)
        return self.convert(request)

    def convert(self, request):
        """Convert a request based on the response type."""
        content_type = request.headers['content-type']
        content = request.content
        if content_type == 'application/json':
            data = json.loads(content)
        elif 'stoplist' in request.url:
            # The `stoplist` endpoint insists that it's HTML.
            data = json.loads(content)
        else:
            data = content
        return data

    def route(self, tag=None, agency=None, **kwargs):
        """
        Get information on a specific route, or all route listings.

        >>> Bongo().route('lantern', 'coralville')
        {"coralville's": {"lantern": "route"}}
        """
        if agency and tag:
            endpoint = 'route'
            kwargs['agency'] = agency
            kwargs['route'] = tag
        else:
            endpoint = 'routelist'
        return self.get(endpoint, **kwargs)

    def routes(self):
        """
        Same as an empty call to the `route` method.

        >>> Bongo().routes()
        {"routes": [1234, 5678, 9999]}
        """
        return self.route()

    def stop(self, number=None, **kwargs):
        """
        Retrieve information specific to a given stop number.

        >>> Bongo().stop(8350)
        {"stop": {"8350": "information"}}
        """
        if number:
            endpoint = 'stop'
            kwargs['stopid'] = number
        else:
            endpoint = 'stoplist'
        return self.get(endpoint, **kwargs)

    def stops(self):
        """
        Same as an empty call to the `stop` method.

        >>> Bongo().stops()
        {"stops": [1234, 5678, 9999]}
        """
        return self.stop()

    def predict(self, number, **kwargs):
        """
        Predict the bus arrival times for a specific stop.

        >>> Bongo().predict(8350)
        {"stop": {"8350": "prediction"}}
        """
        endpoint = 'prediction'
        kwargs['stopid'] = number
        return self.get(endpoint, **kwargs)
