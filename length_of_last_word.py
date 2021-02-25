'''
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。
如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。
示例:
输入: "Hello World"
输出: 5
链接：https://leetcode-cn.com/problems/length-of-last-word
'''

# strip :

def length_of_last_word(s):
    list_s = s.split( )   # 以空格进行分解成一个列表，   split strip方法的使用
    if not list_s:
        return 0
    else:
        return len(list_s[-1])
def length_of_last_word1(s):
    #
    pass


if __name__ == "__main__":
    s  = "Hello World "
    s1 = "a "
    s2 = " "
    print(length_of_last_word(s2))
