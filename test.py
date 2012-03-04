"""
Unit tests for the Bongo API wrapper.
"""

import unittest
from mock import Mock, MagicMock

from bongo import Bongo
from bongo import bongo


def set_up_test(test, content_type="application/json"):
    """A small function for setting up test cases."""
    bongo.req = Mock()
    bongo.json.loads = Mock()
    response = MagicMock()
    response.headers = {'content-type': content_type}
    bongo.req.get.return_value = response
    test.get = bongo.req.get


class BongoInit(unittest.TestCase):

    def test_default_format(self):
        b = Bongo()
        self.assertEqual(b.format, 'json')

    def test_format_can_be_passed_as_argument(self):
        b = Bongo('xml')
        self.assertEqual(b.format, 'xml')


class BongoRoutes(unittest.TestCase):

    def setUp(self):
        set_up_test(self)

    def test_empty_route_method(self):
        b = Bongo()
        b.route()
        params = {'format': 'json'}
        endpoint = 'http://ebongo.org/api/routelist'
        self.get.assert_called_with(endpoint, params=params)

    def test_specific_route(self):
        b = Bongo()
        b.route('lantern', 'coralville')
        params = {'format': 'json', 'route': 'lantern', 'agency': 'coralville'}
        endpoint = 'http://ebongo.org/api/route'
        self.get.assert_called_with(endpoint, params=params)

    def test_routes_method(self):
        b = Bongo()
        b.routes()
        params = {'format': 'json'}
        endpoint = 'http://ebongo.org/api/routelist'
        self.get.assert_called_with(endpoint, params=params)


class BongoStops(unittest.TestCase):

    def setUp(self):
        set_up_test(self)

    def test_empty_stop_method(self):
        b = Bongo()
        b.stop()
        params = {'format': 'json'}
        endpoint = 'http://ebongo.org/api/stoplist'
        self.get.assert_called_with(endpoint, params=params)

    def test_specific_stop(self):
        b = Bongo()
        b.stop('12345')
        params = {'format': 'json', 'stopid': '12345'}
        endpoint = 'http://ebongo.org/api/stop'
        self.get.assert_called_with(endpoint, params=params)

    def test_stop_method_can_take_int_argument(self):
        b = Bongo()
        b.stop(12345)
        params = {'format': 'json', 'stopid': 12345}
        endpoint = 'http://ebongo.org/api/stop'
        self.get.assert_called_with(endpoint, params=params)

    def test_stops_method(self):
        b = Bongo()
        b.stops()
        params = {'format': 'json'}
        endpoint = 'http://ebongo.org/api/stoplist'
        self.get.assert_called_with(endpoint, params=params)


class BongoContentType(unittest.TestCase):

    def setUp(self):
        set_up_test(self, "XML")

    def test_stops_method_with_xml_format(self):
        b = Bongo('xml')
        b.stops()
        self.get.return_value = Mock()
        params = {'format': 'xml'}
        endpoint = 'http://ebongo.org/api/stoplist'
        self.get.assert_called_with(endpoint, params=params)

    def test_stop_method_with_xml_format(self):
        b = Bongo('xml')
        b.stop(8350)
        self.get.return_value = Mock()
        params = {'format': 'xml', 'stopid': 8350}
        endpoint = 'http://ebongo.org/api/stop'
        self.get.assert_called_with(endpoint, params=params)


class BongoPrediction(unittest.TestCase):

    def setUp(self):
        set_up_test(self)

    def test_prediction_for_stop(self):
        b = Bongo()
        b.predict(12345)
        params = {'format': 'json', 'stopid': 12345}
        endpoint = 'http://ebongo.org/api/prediction'
        self.get.assert_called_with(endpoint, params=params)


if __name__ == '__main__':
    unittest.main()
