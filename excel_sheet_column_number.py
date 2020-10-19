'''
给定一个Excel表格中的列名称，返回其相应的列序号。
例如，
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
示例 1:
输入: "A"
输出: 1
示例 2:
输入: "AB"
输出: 28
示例 3:
输入: "ZY"
输出: 701
链接：https://leetcode-cn.com/problems/excel-sheet-column-number
'''

def excel_sheet_column_number(s):
    excel_dict = {'A':1 , 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12,
                  'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23,
                  'X':24, 'Y':25, 'Z':26}
    s_list = list(s)
    num = 0
    for i in range(len(s_list)):
        num = num + excel_dict[s_list[-1]]*26**i
        s_list.pop()
    return num
def excel_sheet_column_number2(s):
    num = 0
    for j in range(len(s)):
        num = num + (ord(s[::-1][j])-64)*26**j

        return num


if __name__ == "__main__":
    s1 = 'A'
    s2 = 'AA'
    s3 = 'ZZ'
    s4 = 'AAA'
    print(excel_sheet_column_number(s2))


'''

#获取ASCII码数字
ord('a')
#ASCII码转为字符
chr(97)
'''