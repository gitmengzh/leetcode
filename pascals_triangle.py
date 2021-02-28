'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
链接：https://leetcode-cn.com/problems/pascals-triangle
'''

def generate(numRows):
    while numRows == 0:
        return []
    while numRows == 1:
        return [[1]]
    while numRows == 2:
        return [[1],[1, 1]]
    res = [[1],[1, 1]]
    for i in range(2, numRows):
        res.append([1])
        for j in range(1, i+1):
            if j < (i):
                res[i].append(res[i-1][j-1]+res[i-1][j])
            else:
                res[i].append(1)


    return res

# 递归超时
class Solution(object):
    def generate(self, numRows: int):


        res = []
        while numRows == 0:
            return res
        for i in range(numRows):
            res.append(self.aaa(i + 1))
        return res

    def aaa(self, n: int):
        res = [1]
        while n == 1:
            return res
        while n == 2:
            return [1, 1]

        for i in range(1, n - 1):
            a = self.aaa(n - 1)[i - 1]
            b = self.aaa(n - 1)[i]
            res.append( a + b )

        return res + [1]
if __name__ == "__main__":
   print(generate(5))