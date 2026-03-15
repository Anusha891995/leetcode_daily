class Fancy(object):

    def __init__(self):
        self.nums = []
        self.a = 1
        self.b = 0
        self.MOD = 10**9 + 7
        

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.nums.append(((val - self.b) * pow(self.a, self.MOD - 2, self.MOD)) % self.MOD)

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.b = (self.b + inc) % self.MOD

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        self.a = (self.a * m) % self.MOD
        self.b = (self.b * m) % self.MOD

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        if idx >= len(self.nums):
            return -1
        return (self.nums[idx] * self.a + self.b) % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)