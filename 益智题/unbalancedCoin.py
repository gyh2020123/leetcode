import random

class UnbalancedCoin:
    def __init__(self, p, rand=None):
        self._p = p
        if rand is None:
            rand = random.Random()
        self._rand = rand

    def Flip(self):
        return self._rand.random < self._p
    
def makeEqualProb(coin):
    while True:
        a = coin.Flip()
        if a != coin.Flip():
            return a

coin = UnbalancedCoin(0.4)
print(makeEqualProb(coin))
