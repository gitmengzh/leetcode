"""
编写一个函数，检查输入的链表是否是回文的。
示例 1：
输入： 1->2    输出： false
示例 2：
输入： 1->2->2->1  输出： true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

链接：https://leetcode-cn.com/problems/palindrome-linked-list-lcci
"""
def isPalindrome1(head):
    temp = head
    res = []
    while temp:
        res.append(temp.val)
        temp = temp.next
    return res == res[::-1]


def isPalindrome2(head):
    pass
