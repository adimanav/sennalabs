class LotteryPerms:
    size = int()

    def __init__(self, size):
        self.size = int(size)

    def output1(self, size):
        result = []
        if size <= 1:
            for i in range(0, 10):
                result.insert(len(result), "" + str(i))
        else:
            for i in range(0, 10):
                tmp = self.output1(size - 1)
                for num in tmp:
                    result.insert(len(result), num + "" + str(i))
        return result

    def output(self):
        return self.output1(self.size)
        
if __name__ == '__main__':
    lc = LotteryPerms(6)
    out = lc.output()
    print(out)
    print("total count: " + str(len(out)))