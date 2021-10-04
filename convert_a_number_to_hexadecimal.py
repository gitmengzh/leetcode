"""
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。
注意:
十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
示例 1：
输入:26
输出:"1a"

示例 2：
输入: -1
输出: "ffffffff"
链接：https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal
"""

# 负数用补码表示: 让任意一个整数 n & 0xFFFFFFFF 就能表示出任意一个数在计算机的表示方式（在计算机中，通常都是采用补码形式）
def toHex(num):
       return hex(num & 0xFFFFFFFF)[2:]                   # hex hex() 函数将指定的数字转换为十六进制值。返回的字符串始终以前缀 0x 开头。


def toHex2(num):
    num &= 0xFFFFFFFF
    s = "0123456789abcdef"
    res = ""
    mask = 0b1111
    while num > 0:
        res += s[num & mask]    # 与mask相与，得到最后四位的数值，转换成s中的内容（16进制表示）
        num >>= 4       # 向右移动思维后的结果，例如17（10001），向右移动四维结果为1
    return res[::-1] if res else "0"

def toHex3(num):
    CONV = "0123456789abcdef"
    ans = []
    # 32位2进制数，转换成16进制 -> 4个一组，一共八组(最大数需要循环次数)
    for _ in range(8):
        ans.append(num % 16)
        num //= 16
        if not num:
            break
    return "".join(CONV[n] for n in ans[::-1])




if __name__ == "__main__":
    num1= 16
    print(toHex(num1))
