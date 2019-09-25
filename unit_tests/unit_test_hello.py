import unittest
from hello import Hello

class TestHello(unittest.TestCase):

    def test_hello(self):
        hello = Hello()
        self.assertEqual(hello.output("Santa Claus"), "Hello, Santa Claus!")

if __name__ == '__main__':
    unittest.main()