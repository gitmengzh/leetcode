"""
给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。若环不存在，请返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

链接：https://leetcode-cn.com/problems/linked-list-cycle-lcci

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def detectCycle1(head):
        set1 = set()   # 用set存储已有链表值，遍历链表，如果存在set中，则证明有环
        cur = head
        while cur:
            if cur not in set1:
                set1.add(cur)
            else:
                return cur
            cur = cur.next


def detectCyle2(head):          # 双指针
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return None

    slow = head
    while slow != fast:             #  https://leetcode-cn.com/problems/linked-list-cycle-lcci/solution/python3-liang-chong-fang-fa-shi-xian-huan-lu-jian-/
        slow = slow.next            # 结论： 起点到环开头的距离等于环内相遇点到环开头点的距离
        fast = fast.next
    return slow


