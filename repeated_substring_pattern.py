'''
459. 重复的子字符串
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
示例 1:
输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。
https://leetcode-cn.com/problems/repeated-substring-pattern/
'''


def repeatedSubstringPattern(s: str) -> bool:
    if len(set(s)) == 1:
        return True
    elif len(set(s)) == len(s):
        return False
    temp = s[0]
    for i in range(1, (len(s) // 2)+1):
        if s[i] != s[0]:
            temp += s[i]
            continue
        else:
            len_temp = i + len(temp)
            end = i
            while len_temp <= len(s):
                if s[end:(end + len(temp))] == temp:
                    if len_temp == len(s):
                        return True
                    end = len_temp
                    len_temp += len(temp)
                else:
                    temp += s[i]
                    break
    return False

def repeatedSubstringPattern2(s: str) -> bool:
    return s in (s + s)[1:-1]

if __name__ == "__main__":
    s = 'abab'
    s1 = 'aaaaaaaaaaaaacccaaaaaaaaaaaaaccc'
    s2 = 'abacabac'
    print(repeatedSubstringPattern2(s1))