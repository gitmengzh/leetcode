'''
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，
所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
示例 1
输入: 3   输出: "III"
示例 2:
输入: 4   输出: "IV"
示例 3:
输入: 9   输出: "IX"
示例 4:
输入: 58   输出: "LVIII"
解释: L = 50, V = 5, III = 3.
示例 5:
输入: 1994   输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
链接：https://leetcode-cn.com/problems/integer-to-roman
'''
# 思路： 将数字转化程字符串，然后从最后一位开始遍历，0不考虑，如果数字在字典中有对应值，则返回对应值且乘系数，
# 设置系数i=0，每次循环过后加1，10的i次方为系数
# 分别对4，9，【2，3】， 【6，7，8】进行处理
def integer_to_number(num):
    r_dict = {'1':'I', '5':'V', '10':'X', '50':'L', '100':'C', '500':'D', '1000':'M'}
    roman = []
    str_nums = str(num)
    i = 0
    for j in str_nums[::-1]:
        if str(int(j)*(10**i)) in r_dict.keys():
            roman.append(r_dict.get(str(int(j)*10**i)))
        elif j == '4':
            roman.append(r_dict.get(str(1*10**i))+r_dict.get(str(5*10**i)))
        elif j == '9':
            roman.append(r_dict.get(str(1*10**i))+r_dict.get(str(10**(i+1))))
        elif j in ['2','3']:
            roman.append((r_dict.get(str(10**i)))*int(j))
        elif j in ['6','7','8']:
            roman.append(r_dict.get(str(5*10**i))+(r_dict.get(str(10**i)))*(int(j)-5))
        i=i+1

    result = "".join(roman[::-1])
    return result


def integer_to_number2(num):
    d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
         4: 'IV', 1: 'I'}
    result = ''
    for i in d:
        while num > i:
            num = num-i
            result = result + d.get(i)
    return result







if __name__ == "__main__":
    num1 = 3
    num2 = 4
    num3 = 9
    num4 = 58
    num5 = 1994
    num6 = 44
    print(integer_to_number(num5))
   #  a = [1]
   #  a.insert(0,1)
   #  print(a)
