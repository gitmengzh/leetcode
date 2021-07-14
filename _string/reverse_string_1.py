'''
将字符串中的单词进行反转，然后输出
eg:
    input:'I am a Student.'
    output:'student. a am I'

https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/
'''


class Solution(object):

    @staticmethod
    def reverse_string(s: str):
        new_s = s.strip()  # 去掉收尾空格
        new_list = new_s.split(' ')
        res = ' '.join(new_list[::-1])
        return res

    @staticmethod
    def reverse_string2(s: str):  # 将每个字符串反转，再整体反转
        new_s = s.strip()
        for i in new_s:
            reversed(i)
        new_list = new_s.split(' ')
        new_list.reverse()
        return ' '.join(new_list)



if __name__ == "__main__":
    s1 = ' I am a Student.  '
    s2 = ''
    print(Solution.reverse_string2(s1))
