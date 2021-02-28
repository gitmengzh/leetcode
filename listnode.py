'''

用python实现一个链表
'''


# # 链表节点类
# class ListNode():
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
#
# # 单链表
# class Singlelist():
#     def __init__(self, item):
#         self.item = item
#         """
#             self.length   用于记录链表的长度
#             self.head     链表的头部
#             self.tail     记录链表的尾部
#             """
#
#         def __init__(self, item):
#             """
#             item   一位数组，存放改链表的数组
#
#             """
#             self.length = len(item)
#             if self.length <= 0:
#                 return
#             i = 0
#             self.head = linkNode(item[i])
#             self.tail = self.head
#             i += 1  ###此句不能少
#             while i < self.length:
#                 self.tail.next = linkNode(item[i])
#                 self.tail = self.tail.next
#                 i += 1

 # 链表节点
class Node(object):
    def __init__(self, data, address=None):
        self.data = data
        self.next = address

# 链表
class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    # 向链表追加节点
    def add(self, data):
        if self.length:
            node = self.head
            while node.next:
                node = node.next
            else:
                node.next = Node(data)
        else:
            self.head = Node(data)
        self.length += 1

    # 返回指定索引节点
    def get(self, index):
        if index >= self.length:
            raise(IndexError, "list index out of range.")
        node = self.head
        while index:
            node = node.next
            index -= 1
        return node

    # 删除一个节点
    def delete(self, index):
        if index == 0:
            self.head = self.head.next
        elif index == self.length-1:
            self.get(index-1).next = None
        else:
            self.get(index - 1).next = self.get(index+1)
        self.length -= 1

    # 在指定索引位置插入一个节点
    def insert(self, index, data):
        if index == 0:
            self.add(data)
        else:
            node = Node(data, self.get(index))
            self.get(index - 1).next = node
        self.length += 1

    # 遍历链表中的节点值
    def traverse(self):
        value = list()
        node = self.head
        while node:
            value.append(node.data)
            node = node.next
        return value


if __name__ == "__main__":
    linked = LinkedList()
    for i in range(10):
        linked.add(i)
    print("LinkedList: {}".format(linked.traverse()))
    print("GetNode(2): {}".format(linked.get(2)))
    linked.delete(2)
    print("LinkedList(after delete(2): {}".format(linked.traverse()))
    linked.insert(2, "a")
    print("LinkedList(after insert(2, a): {}".format(linked.traverse()))