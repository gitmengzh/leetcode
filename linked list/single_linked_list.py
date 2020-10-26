'''
实现单链表
'''
# 定义节点
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class Singlelinklist(object):
    def __init__(self, node=None):
        self.head = node   # 初始化头节点，并给节点默认为None

    # 判断链表是否为空，头节点为None
    def is_empty(self):
        return self.head == None

    # 链表长度
    def length(self):
        cur = self.head  # 当前节点位置
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    # 链表头部插入节点
    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node


    # 链表尾部添加节点
    def append(self, item):
        node = Node(item)
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    # 链表任意位置插入
    def insert(self, pos, elem):
        node = Node(elem)
        pre = self.head
        if pos <= 0:
            self.add(elem)
        elif pos > (self.length()-1):
            self.append(elem)
        else:
            count = 0
            while count < pos:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node


    # 查找
    def search(self, item):
        cur = self.head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        # res = None
        cur = self.head
        pre = None
        while cur.elem != None: #  当前节点为None, 结束循环
            if cur.elem == item:
                if cur == self.head:
                    res = cur.elem
                    self.head = cur.next  #  如果要删除的元素为头元素，那么直接把头节点指向cur.next
                else:
                    res = cur.elem
                    pre.next = cur.next
                return res
            else:
                pre = cur
                cur = cur.next



if __name__ == "__main__":
    node  = Singlelinklist()
    node.append(1)
    # print(node.travel(), end="")
    node.add(3)
    # print(node.travel())

    node.insert(1,2)
    # print(node.travel())

    # print(node.length())

    # print(node.search(3))
    node.remove(1)
    print(node.travel())
