def reverseEvenLengthGroups(head) :
    if not head.next or not head.next.next:
        return head
    num1 = num2 = 2     # 定义启示为2
    cur = head
    start = head.next
    end = head.next

    while True:
        if num1 % 2 == 0:
            while end and num2:
                end = end.next
                num2 -= 1


    cur1 = cur2 = cur3 = head.next
    pre = head

    t_cont1 = t_cont2 = 2
    while cur1:
        while t_cont1 and cur2:
            t_cont1 -= 1
            pre = cur2
            cur2 = cur2.next
            if t_cont1 >= 1 and not cur2:
                return head
            elif t_count1 == 0 and (t_cont2 % 2) == 0:
                pre = self.reverselist(cur1)

            cur1 = cur2
        t_cont2 += 1
        t_cont1 = t_cont2

    return head


def reverselist(self, pre, cur):
    while cur:
        pre, cur.next, cur = cur, pre, cur.next

    return pre

