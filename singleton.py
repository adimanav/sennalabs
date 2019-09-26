class Singleton(object):
  _instances = {}
  def __new__(class_, *args, **kwargs):
    if class_ not in class_._instances:
        class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
    return class_._instances[class_]

class FootballScore(Singleton):
    _score1 = 0
    _score2 = 0

    def incrementScore1(self):
        self._score1 += 1

    def incrementScore2(self):
        self._score2 += 1

    def getScore1(self):
        return self._score1

    def getScore2(self):
        return self._score2

if __name__ == "__main__":
    fs1 = FootballScore()
    fs2 = FootballScore()
    fs1.incrementScore1()
    fs1.incrementScore2()
    fs2.incrementScore1()
    fs2.incrementScore2()
    print("Score 1: " + str(fs1.getScore1()))
    print("Score 2: " + str(fs1.getScore2()))
    print("Score 1: " + str(fs2.getScore1()))
    print("Score 2: " + str(fs2.getScore2()))

    