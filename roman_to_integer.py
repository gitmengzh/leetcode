'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
链接：https://leetcode-cn.com/problems/roman-to-integer
思路：
    首先取字符串第一个值，赋值给A，
    然后将第一个值移除，判断A 与剩余字符串的第一个值B大小
    如果A比B小，相减，并移除B
    否则将A对应的值赋值给result
    注意 字符串长度，当等于0时，break
    付过字符串长度等于1， 那么直接输出

'''


def romanToInt(s):
    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L':50,'C':100, 'D':500, 'M':1000}
    roman = list(s)  # 转列表
    result = 0
    for i in range(len(roman)):
        if len(roman) == 0:     # 长度等于0，停止
            break
        if len(roman)==1:       # 长度等于1， 直接输出结果
            result = result + r_dict.get(roman[0])
            roman.pop(0)
        else:
            roman_value = roman[0]
            roman.pop(0)
            if r_dict.get(roman_value) < r_dict.get(roman[0]):   # 判断字符串是否小于它右边的值
                result = result + r_dict.get(roman[0]) - r_dict.get(roman_value)
                roman.pop(0)
            else:
                 result = result+r_dict.get(roman_value)


    return result





if __name__ == "__main__":
    s1 = 'II'
    s2 = "IV"
    s3 = "LVIII"
    s4 = "MCMXCIV"
    s5 = "MCMXCVI"
    print(romanToInt(s5))