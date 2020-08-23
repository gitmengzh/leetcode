'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 限制：
0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
'''

def solution(matrix):

#     res = []
#     while matrix:
#         res += matrix.pop(0)
#         matrix = list(zip(*matrix))[::-1]
#     return res
#
#
# test_list = [[1,2,3],[4,5,6],[7,8,9]]
# test = solution(test_list)
# print(test)
    if not matrix:
        return []

    a, b, c, d = 0, 0, len(matrix[1]), len(matrix)-1
    res = []
    for i in matrix[a]:
        res.append(a)
    i

