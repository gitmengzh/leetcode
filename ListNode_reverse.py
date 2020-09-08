'''
反转链表

'''
def listnode_reverse1(head):
    if not head or not head.next:
        return head
    Node = None
    while head:
        p = head
        head = head.next
        p.next = Node
        Node = p
    return Node

def listnode_reverse2(head):
    if not head:
        return None
    prev = None
    cur = head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return cur

def listnode_reverse13(head):
    stack = [None]
    while head:
        stack.append(head)
        head = head.next
    head = stack.pop()
    cur = head
    while stack:
        cur.next = stack.pop()
        cur = cur.next
    return head


if __name__ == "__main__":
    l = [1,2,3,4,5]
    print(listnode_reverse1(l))
