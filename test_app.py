import json
import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_setBoard(self):
        # A good request should return 200
        good_board = '{"board": [["a", "b"], ["c", "d"]]}'

        rv = self.client.post('/board',
                              data=good_board,
                              content_type='application/json')
        self.assertEqual(rv.status_code, 200)

        # A request with no board should return 400
        rv = self.client.post('/board',
                              content_type='application/json')
        self.assertEqual(rv.status_code, 400)

        # A request with a non-alpha character should return 400
        bad_board = '{"board": [["a", "b"], ["1", "d"]]}'

        rv = self.client.post('/board',
                              data=bad_board,
                              content_type='application/json')
        self.assertEqual(rv.status_code, 400)

        # A list that includes a nonstring value should return 400
        bad_board = '{"board": [["a", "b"], ["c", 1]]}'

        rv = self.client.post('/board',
                              data=bad_board,
                              content_type='application/json')
        self.assertEqual(rv.status_code, 400)

    def test_searchBoard(self):
        test_board = '{"board": [["a", "b"], ["c", "d"]]}'

        self.client.post('/board',
                         data=test_board,
                         content_type='application/json')

        rv = self.client.get('/search/test,something,ac')
        results = json.loads(rv.data)
        self.assertEqual(results['results'], ['ac'])


if __name__ == '__main__':
    unittest.main()
