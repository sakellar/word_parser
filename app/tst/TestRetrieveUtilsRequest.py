import unittest
from mock import patch, Mock, MagicMock, call
from retrieve_utils import Request


class TestRetrieveUtilsRequest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('retrieve_utils.requests')
    def test_get_http_message(self, mock_requests):
        mock_requests.request.return_value.status_code = 200
        mock_requests.request.return_value.text = "whatever"
        mock_requests.request.return_value.headers = "whatever"
        retrieve_obj = Request("http://a_url1")
        res = retrieve_obj.get_request()
        mock_requests.assert_has_calls([call.request(method='GET', url="http://a_url1")])
        self.assertEqual(res[0], 200)
        self.assertEqual(res[1], "whatever")
        self.assertEqual(res[2], "whatever")

if __name__ == '__main__':
    unittest.main(buffer=False)
