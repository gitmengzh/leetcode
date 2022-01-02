"""
给你一个 仅 由字符 'a' 和 'b' 组成的字符串  s 。如果字符串中 每个 'a' 都出现在 每个 'b' 之前，返回 true ；否则，返回 false 。
示例 1：
输入：s = "aaabbb"
输出：true
解释：
'a' 位于下标 0、1 和 2 ；而 'b' 位于下标 3、4 和 5 。
因此，每个 'a' 都出现在每个 'b' 之前，所以返回 true 。
示例 2：
输入：s = "abab"
输出：false
解释：
存在一个 'a' 位于下标 2 ，而一个 'b' 位于下标 1 。
因此，不能满足每个 'a' 都出现在每个 'b' 之前，所以返回 false 。
示例 3：
输入：s = "bbb"
输出：true
解释：
不存在 'a' ，因此可以视作每个 'a' 都出现在每个 'b' 之前，所以返回 true 。
提示：
    1 <= s.length <= 100
    s[i] 为 'a' 或 'b'
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-all-as-appears-before-all-bs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

def checkString(s):
    # list_s = list(s)
    # if len(set(list_s)) == 1:
    #     return True
    # else:
    #     return True if (len(list_s)-list_s[::-1].index('a')-1) < list_s.index('b') else False
    return not any(a == 'b' and b == 'a' for a, b in zip(s, s[1:]))
    # return 'ba' not in s
if __name__ == "__main__":
    s = "bbb"
    print(checkString(s))







