"""
句子是由若干 token 组成的一个列表，token 间用 单个 空格分隔，句子没有前导或尾随空格。每个 token 要么是一个由数字 0-9 组成的不含前导零的 正整数 ，要么是一个由小写英文字母组成的 单词 。
    示例，"a puppy has 2 eyes 4 legs" 是一个由 7 个 token 组成的句子："2" 和 "4" 是数字，其他像 "puppy" 这样的 tokens 属于单词
给你一个表示句子的字符串 s ，你需要检查 s 中的 全部 数字是否从左到右严格递增（即，除了最后一个数字，s 中的 每个 数字都严格小于它 右侧 的数字）。
如果满足题目要求，返回 true ，否则，返回 false 。

链接：https://leetcode-cn.com/problems/check-if-numbers-are-ascending-in-a-sentence


"""
def areNumbersAscending(s):
    temp = s.split(' ')
    a = [str(j) for j in range(2, 101)]
    b = 0
    for i in temp:
        if i in a and int(i) > b:
            b = int(i)
        elif i in a and int(i) <= b:
            return False

    return True

def areNumbersAscending2(s):
    temp = s.split(' ')
    res = 0
    for i in temp:
        if i.isdigit() and int(i) > res:    # isdigit() 方法检测字符串是否只由数字组成。
            res = int(i)
        elif i.isdigit() and int(i) <= res:
            return False
    return True






if __name__ == "__main__":
    s = "this is 1 2"
    print(areNumbersAscending2(s))

