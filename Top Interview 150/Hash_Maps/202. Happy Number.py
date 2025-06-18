class Solution:
    def isHappy(self, n: int) -> bool:
        dic = {}
        while n != 1 and n not in dic:
            dic[n] = sum(int(digit)**2 for digit in str(n)) #generator expression
            n = dic[n]
        return n == 1