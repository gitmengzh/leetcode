'''
验证回文串
只验证字母和数字
不区分大小写
空串返回true
返回：
如果是回文串返回true
否则返回false
注：
回文串指是一个正读和反读都一样的字符串
'''
import re
# 初始思路：遍历整个字符串，首先将大转成小写，然后写到列表中，如果不是数字或者字母，不加入列表，然后转成字符串比较
# 缺点：效率低
# 使用方法： isalnum（） 判断是不是字母或者数字    isupper()判断是不是大写字母   string.lower()转小写
# ''.join([str(x) for x in list])   list转str， string.upper()小写转大写
def valid_palindrome(s):
    new_s = []
    new_j = []
    if not s:
        return True
    j = s[::-1]
    for a in s:
        if a.isalnum():
            if a.isupper():
                new_s.append(a.lower())
            else:
                new_s.append(a)
    for b in j:
        if b.isalnum():
            if b.isupper():
                new_j.append(b.lower())
            else:
                new_j.append(b)

    str_s =''.join([str(x) for x in new_s])
    str_j =''.join([str(x) for x in new_j])
    if str_s == str_j:
        return True
    else:
        return False
# 第二种方法，直接定义一个空字符串，还是使用isalnum（）函数判定，如果不是字母和数字挑过，如果是，那么继续判定是否为大写
# 如果是大写，那么转成小写添加，否则直接添加， 内存和运行时间都大大缩短
def valid_palindrome1(s):
    j = ''
    if not s:
        return True
    for i in s:
        if i.isalnum():
            if i.isupper():
                j = j+i.lower()
            else:
                j = j+i
    if j == j[::-1]:
        return True
    else:
        return False

# 网友方法用正则解决
def valid_palindrome2(s):
    s = re.sub(r'[^a-z0-9]', '', s.strip().lower())
    return s == s[::-1]


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    s1 =  "race a car"
    print(valid_palindrome2(s1))

'''
字符串.isalnum()	所有字符都是数字或者字母，为真返回 Ture，否则返回 False。
字符串.isalpha() 	所有字符都是字母，为真返回 Ture，否则返回 False。
字符串.isdigit() 	所有字符都是数字，为真返回 Ture，否则返回 False。
字符串.islower()	所有字符都是小写，为真返回 Ture，否则返回 False。
字符串.isupper()	所有字符都是大写，为真返回 Ture，否则返回 False。
字符串.istitle()	所有单词都是首字母大写，为真返回 Ture，否则返回 False。
字符串.isspace()	所有字符都是空白字符，为真返回 Ture，否则返回 False。
'''


