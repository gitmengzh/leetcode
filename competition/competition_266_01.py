"""

字符串 是字符串中的一个连续（非空）的字符序列。

元音子字符串 是 仅 由元音（'a'、'e'、'i'、'o' 和 'u'）组成的一个子字符串，且必须包含 全部五种 元音。

给你一个字符串 word ，统计并返回 word 中 元音子字符串的数目 。



示例 1：

输入：word = "aeiouu"
输出：2
解释：下面列出 word 中的元音子字符串（斜体加粗部分）：
- "aeiouu"
- "aeiouu"

示例 2：

输入：word = "unicornarihan"
输出：0
解释：word 中不含 5 种元音，所以也不会存在元音子字符串。

示例 3：

输入：word = "cuaieuouac"
输出：7
解释：下面列出 word 中的元音子字符串（斜体加粗部分）：
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"

示例 4：

输入：word = "bbaeixoubb"
输出：0
解释：所有包含全部五种元音的子字符串都含有辅音，所以不存在元音子字符串。



提示：
    1 <= word.length <= 100
    word 仅由小写英文字母组成

"""


def countVowelSubstrings(word):
    if len(word) < 5:
        return 0
    temp1 = ['a', 'e', 'i', 'o', 'u']
    temp2 = []
    slow = 0
    res = 0
    while slow <= len(word)-5:
        if word[slow] in temp1:
            for fast in range(slow, len(word)):
                if word[fast] in temp1 and word[fast] not in temp2:
                    temp2.append(word[fast])
                    fast += 1
                    if len(temp2) ==5:
                        res += 1

                elif word[fast] in temp1 and word[fast] in temp2 and len(temp2) == 5:
                    fast += 1
                    res += 1
                elif word[fast] in temp1 and word[fast] in temp2:
                    continue
                else:
                    break
            slow += 1
            temp2 = []
        else:
            slow += 1
    return res

if __name__  == "__main__":
    word1 = 'auioe' # 1
    word2 = 'aeioua'    # 3
    word3 = 'aaa'   # 0
    word4 = 'ccccaeiou' # 1
    word5 = ''  # 0
    word6 = 'aeiouu'
    word7 = 'cuaieuouac'
    print(countVowelSubstrings(word6))