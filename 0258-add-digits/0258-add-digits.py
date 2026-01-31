class Solution:
    def addDigits(self, num: int) -> int:
        add = 0
        if num <= 9: return num
        while num > 0:
            add += num %10
            num = num//10
        return self.addDigits(add)
        