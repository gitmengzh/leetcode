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
    # 广度优先遍历
    def bfs(self):
        if self.root is None:
            return self.root   # 如果根节点为空，则返回空
        queue = [self.root]    # 定义一个列表
        while queue:        # 知道队列为空，即没有左右子节点加入到队列，则完成遍历
            curnode = queue.pop(0)  # 当前节点为列表的第一个值
            print(curnode.elem)     # 打印当前节点的元素
            if curnode.lchid is not None:   # 如果当前节点的左节点不为空
                queue.append(curnode.lchid)     # 将当前节点的左节点加入到队列
            if curnode.rchid is not None:   # 如果当前节点的右节点不为空
                queue.append(curnode.rchid)     # 将当前节点的又节点加入到队列

    # 深度优先遍历，分为先序遍历、中序遍历、后序遍历
    # 先序： 根、左、右
    def preorder(self, node):   # 三种遍历用到了递归，基本一致，以先序遍历为例解释
        while node is None:     # 当节点等于空时，停止递归
            return None
        print(node.elem)        # 输出当前节点
        self.preorder(node.lchid)   # 当前节点的左节点调用此函数，然后打印左节点
        self.preorder(node.rchid)   # 当前节点的右节点调用此函数

    # 中序： 左、根、右
    def midorder(self, node):
        while node is None:
            return None
        self.midorder(node.lchid)
        print(node.elem)
        self.midorder(node.rchid)

    # 后序： 左、右、根
    def postorder(self, node):
        while node is None:
            return None
        self.postorder(node.lchid)
        self.postorder(node.rchid)
        print(node.elem)

    def symmetric_tree(self):
        while self.root is None:
            return True



if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    # tree.bfs()
    tree.preorder(tree.root)

