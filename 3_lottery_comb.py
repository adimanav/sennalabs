class LotteryComb:
    num = int()

    def __init__(self, num):
        self.num = int(num)

    def output(self):
        rem = int(self.num % 100)
        fact = int(self.num / 100)
        out = []
        for left in range(0, fact):
            count = len(str(left))
            pad = 4 - count
            padding = ""
            for i in range(0, pad):
                padding += "0"
            out.append(padding + str(left) + str(rem))
        return out

lc = LotteryComb(120888)
out = lc.output()
print(out)