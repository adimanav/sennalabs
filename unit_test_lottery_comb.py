import unittest
from lottery_comb import LotteryComb

class TestLotteryComb(unittest.TestCase):

    def output(self, num):
        rem = int(num % 100)
        fact = int(num / 100)
        out = []
        for left in range(0, fact):
            count = len(str(left))
            pad = 4 - count
            padding = ""
            for i in range(0, pad):
                padding += "0"
            out.append(padding + str(left) + str(rem))
        return out

    def test_output(self):
        lc = LotteryComb(120888)
        self.assertEqual(lc.output(), self.output(120888))

if __name__ == '__main__':
    unittest.main()