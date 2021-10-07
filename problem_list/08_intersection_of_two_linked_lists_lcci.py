"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/
"""
def getIntersectionNode(headA, headB):
    a = headA
    b = headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a


