'''
翻转二叉树
'''
def aaa(n):
    ans = 0
    for i in range(31, -1, -1):  # 从31到0
        temp = (n & 1) << i  # (提取最低位)<<左移到第i位
        ans += temp  # 加给结果
        n >>= 1  # n的最低位处理完了，换下一个
    return ans
n= 0b00000010100101000001111010011100
# print(aaa(n))
a= '5'
print(int(a, 2))