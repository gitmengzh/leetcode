'''
给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
示例 1:
输入: s = "egg", t = "add"
输出: true
示例 2:
输入: s = "foo", t = "bar"
输出: false
示例 3:
输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。
链接：https://leetcode-cn.com/problems/isomorphic-strings

'''
# 思路：设置两个新的字符串，遍历两个老的字符串，如果元素在新的字符串中，记录新字符串的位置，如果不在，则记录元素在老字符串的位置
# 对将对应的字符加到新字符串当中，如果最后记录的坐标一致，那么则判定
def isomorphic_strings(s,t):
    # if not s and not t:
    #     return True
    nums_s = ''
    nums_t = ''
    key_v1 = ''
    key_v2 = ''
    for i in s:
        if i in nums_s:
            key_v1 = key_v1 + str(nums_s.index(i))
        else:
            key_v1 = key_v1 + str(s.index(i))
        nums_s = nums_s + i
    for j in t:
        if j in nums_t:

            key_v2 = key_v2+str(nums_t.index(j))
        else:

            key_v2 = key_v2+str(t.index(j))
            nums_t = nums_t + j
    if key_v1 == key_v2:
        return True
    else:
        return False
# 使用zip函数可以同时遍历两个字符串
def isomorphic_strings1(s,t):
    # if not s and not t:
    #     return True
    nums_s = ''
    nums_t = ''
    key_v1 = ''
    key_v2 = ''
    for i,j in zip(s, t):
        if i in nums_s and j in nums_t:
            key_v1 = key_v1 + str(nums_s.index(i))
            key_v2 = key_v2 + str(nums_t.index(j))
        else:
            key_v1 = key_v1 + str(s.index(i))
            key_v2 = key_v2 + str(t.index(j))
            nums_t = nums_t + j
            nums_s = nums_s + i
    if key_v1 == key_v2:
        return True
    else:
        return False

def hashing(s,t):
    if not s:
        return True
    dic = {}
    for i in range(len(s)):
        if s[i] not in dic:
            if t[i] in dic.values():
                return False
            else:
                dic[s[i]] = t[i]
        else:
            if dic[s[i]] != t[i]:
                return False
    return True

def solve4(s,t):
    for i in range(len(s)):
        if s.index(s[i]) != t.index(t[i]):
            return False
    return True


if __name__ == "__main__":
    s1= "paper"
    t1 = "title"
    s2 = "foo"
    t2 = "bar"
    s3 = "ab"
    t3 = "aa"
    s4 = "aa"
    t4 = "ab"
    s5 = "a"
    t5 = "b"
    s6 = ""
    t6 = ""
    print(isomorphic_strings(s1,t1))