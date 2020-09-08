'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

输入: "()"
输出: true
输入: "()[]{}"
输出: true
输入: "(]"
输出: false
输入: "([)]"
输出: false
输入: "{[]}"
输出: true

链接：https://leetcode-cn.com/problems/valid-parentheses


'''
def valid_parentheses(s):
    stack = []
    s_dict = {'}': '{', ']': '[', ')': '('}
    for i in s:
        if stack and stack[-1] == s_dict.get(i):
            stack.pop()
        else:
            stack.append(i)
    return not stack

if __name__ == "__main__":
    s1 = '[{]}'
    s2 = '{}'
    s3 = '{{{}}}'
    s4 = '(]'
    print(valid_parentheses(s1))
