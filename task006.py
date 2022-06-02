class MinecraftBox:
    def __init__(self, lh, wh, ht):
        self.lh = lh
        self.wh = wh
        self.ht = ht

    def volume(self):
        return self.lh * self.wh * self.ht

    def __eq__(self, other):
        return self.volume() == other.volume()
    def __ne__(self, other):
        return self.volume() != other.volume()
    def __lt__(self, other):
        return self.volume() < other.volume()
    def __gt__(self, other):
        return self.volume() > other.volume()
    def __le__(self, other):
        return self.volume() <= other.volume()
    def __ge__(self, other):
        return self.volume() >= other.volume()



Box1 = MinecraftBox(12, 5, 4)
Box2 = MinecraftBox(4, 7, 10)
print(Box1 >= Box2)
print(Box1 <= Box2)
print(Box1 == Box2)
print(Box1 != Box2)
print(Box1 > Box2)
print(Box1 < Box2)