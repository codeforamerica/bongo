"""
Simplified methods for interacting with Bongo's API.
"""

from .core import Bongo


def predict(number, **kwargs):
    """
    Predict the bus arrival times for a specific stop.

    >>> bongo.predict(8350)
    {"stop": {"8350": "prediction"}}
    """
    return Bongo().predict(number, **kwargs)


def route(tag=None, agency=None, **kwargs):
    """
    Get information on a specific route.

    >>> bongo.route('lantern', 'coralville')
    {"coralville's": {"lantern": "route"}}
    """
    return Bongo().route(tag, agency, **kwargs)


def routes():
    """
    Retrieve available routes information.

    >>> bongo.routes()
    {"routes": [1234, 5678, 9999]}
    """
    return Bongo().routes()


def stop(number=None, **kwargs):
    """
    Retrieve information specific to a given stop number.

    >>> bongo.stop(8350)
    {"stop": {"8350": "information"}}
    """
    return Bongo().stop(number, **kwargs)


def stops():
    """
    Retrieve all available stops.

    >>> bongo.stops()
    {"stops": [1234, 5678, 9999]}
    """
    return Bongo().stops()
