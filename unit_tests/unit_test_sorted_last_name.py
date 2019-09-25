import unittest
from sorted_last_name import SortedLastName

class TestSortedLastName(unittest.TestCase):

    def test_output(self):
        sln = SortedLastName("names.csv")
        expected = [
            "Frodo Baggins",
            "Bill Gates",
            "Steve Jobs",
            "Michael Jordan",
            "Barack Obama",
            "Christian Ronaldo",
            "Michael Schumacher",
            "Tiger Woods"
        ]
        self.assertEqual(sln.output(), expected)

if __name__ == '__main__':
    unittest.main()