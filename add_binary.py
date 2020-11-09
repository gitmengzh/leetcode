'''
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。
示例 1:
输入: a = "11", b = "1"
输出: "100"
示例 2:
输入: a = "1010", b = "1011"
输出: "10101"）
链接：https://leetcode-cn.com/problems/add-binary

'''

def add_binary(a,b):
    # 如果字符串长度不相等，用0补全
    if len(a)>=len(b):
        b = '0' * abs(len(a) - len(b))+b
    else:
        a = '0' * abs(len(a) - len(b))+a
    res = ''
    l1 = list(a)
    l2 = list(b)
    temp = '0' # 根据进位情况存储，如果进位，则等于‘01’,如果不进位，就等于相加结果
    for i in range(max(len(a), len(b))):
        s = l1.pop()+l2.pop()
        if s == '00':
            if temp == '0':
                res+='0'
            else:
                res += '1'
                temp = '0'
        elif s =='01' or s == '10':
            if temp == '01': # 如果temp = 01,说明原来有进位，那么这时候应该相加还有进位
                res += '0'
                temp = '01'
            elif temp == '1':
                res += '1'
            else:
                res += '1'
        else:
            if temp == '01':
                res += '1'
            elif temp =='1':
                res += '1'
                temp = '01'
            else:
                temp = '01'
                res+='0'
    if temp == '01':  # 如果temp最后等与01，那么说明有进位，需要加上，
        return (res+temp[-1])[::-1]
    else:
        return res[::-1]
def add_binary2(a,b):
    return bin((int(a,2))+(int(b,2)))[2:]
    # python 内置方法： int()字符串转int型，后边跟进制
    # bin 方法，将一个整数转化为一个二进制整数，并以字符串的类型返回。
if __name__ == "__main__":
    # a = "11"
    # b = "01"
    # a = "1010"
    # b = "1011"
    a = "10111"
    b = "01111"
    print(add_binary(a, b))