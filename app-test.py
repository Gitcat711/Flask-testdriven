from app import app
import unittest

class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/test')
        self.assertEqual(repsonse.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')


if __name == '__main__':
    unittest.main()



