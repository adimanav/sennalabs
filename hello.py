class Hello:
    def output(self, str):
        return "Hello, " + str + "!"

if __name__ == '__main__':
    hello = Hello()
    print(hello.output("Santa Claus"))
