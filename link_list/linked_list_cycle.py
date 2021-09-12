'''
环形链表
给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，
我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false 。
进阶：
你能用 O(1)（即，常量）内存解决此问题吗？
示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
链接：https://leetcode-cn.com/problems/linked-list-cycle
'''

def hasCycle(head):
    if not head or not head.next:       # 如果head 和 head.next 有一个不存在，那么直接返回False
        return False
    slow = head
    fast = head.next
    while fast and fast.next:       # 如果fast 和 fast.next 同时有值，那么循环继续
        if slow == fast:            #  如果有环，那么迟早 slow 和 fast 会相等
            return True
        slow = slow.next            # slow每次进一位
        fast = fast.next.next       # fast 每次进两位
    return False