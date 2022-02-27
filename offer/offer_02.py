# https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/

'''
栈： 先进后出
队列：  先进先出
使用python 的list模拟栈，那么pop()返回最后一个元素
min最小值正常时间复杂度为N，即遍历所有元素，找到最小，要变成O(1), 需要另外找空间存储最小值

'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        if not self.stack2 or self.stack2[-1] <= x:
            self.stack2.append(x)

    def pop(self) -> None:
        if self.stack1.pop() == self.stack2[-1]:
            self.stack2.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def min(self) -> int:
        return self.stack2[-1]





