"""
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
示例1:
 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3
示例2:
 输入：[1, 1, 1, 1, 2]
 输出：[1, 2
提示：
    链表长度在[0, 20000]范围内。
    链表元素在[0, 20000]范围内。
进阶：
如果不得使用临时缓冲区，该怎么解决？
链接：https://leetcode-cn.com/problems/remove-duplicate-node-lcci
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head):
        if not head or not head.next:           # 如果链表为空或者只有一个元素，直接返回
            return head
        val = {head.val}                        # 用set保存已有结果，默认先把head。val加进去
        temp = head
        while temp.next:                        # 直接枚举前驱节点 u，那么节点本身就是 u.next，后继节点就是 u.next.next。
            if temp.next.val in val:
                temp.next = temp.next.next
            else:

                temp = temp.next
                val.add(temp.val)

        return head
