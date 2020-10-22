'''
二叉树的实现
https://www.bilibili.com/video/BV1ZW411q7eK?p=2
用广度优先实现
'''

# 定义一个节点类
class Node(object):
    def __init__(self, item):
        self.elem = item    # 当前节点
        self.lchid = None   # 节点的左子节点
        self.rchid = None   # 节点的右子节点

class Tree(object):
    def __init__(self):
        self.root = None  # 定义根节点

    def add(self, item):
        node = Node(item)   # 构造成一个节点
        if self.root is None:
            self.root = node
            return
        queue = [self.root]     # 将根节点放到队列中
        while queue:
            cur_node = queue.pop(0)  # 当前节点
            if cur_node.lchid is None:
                cur_node.lchid = node
                return
            else:
                queue.append(cur_node.lchid)
            if cur_node.rchid is None:
                cur_node.rchid = node
                return
            else:
                queue.append(cur_node.rchid)


