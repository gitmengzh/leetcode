'''


'''

class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        if x < 0:
            num = int('-'+str(y)[::-1])
        else:
            num = int(str(y)[::-1])
        if -2**31 < num and num <2**31-1:
            return num
        else:
            return 0