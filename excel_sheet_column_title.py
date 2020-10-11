'''
给定一个正整数，返回它在 Excel 表中相对应的列名称。
例如，
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
示例 1:
输入: 1
输出: "A"
示例 2:
输入: 28
输出: "AB"
示例 3:
输入: 701
输出: "ZY"
链接：https://leetcode-cn.com/problems/excel-sheet-column-title
'''

def excel_sheet_column_title(num):
    excel_dict = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}

    # if num < 29:
    #     return excel_dict.get(num)
    # # while num//26>1:
    # #     res = num//26
    # #     num = num%26
    # #     if num <
    # #     res = res+excel_dict.get(res)
    # else:
    #     a = num // 26
    #     b = num%26
    #     if b ==0:
    #         res = excel_dict.get(a-1)+'Z'
    #     else:
    #         res = excel_dict.get(a) + excel_dict.get(b)
    #     return res
    res = ''




if __name__ == "__main__":
    num1 = 1
    num2 = 701
    num3 = 52 #AZ
    num4 = 703 #AZZ
    print(excel_sheet_column_title(num4))