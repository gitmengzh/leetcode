# https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/

'''
栈： 先进后出
队列：  先进先出
使用python 的list模拟栈，那么pop()返回最后一个元素


'''
class CQueue:

    def __init__(self):
        self.A, self.B = [], []   # 定义两个栈

    def appendTail(self, value: int) -> None:           # 定义添加队尾操作
        self.A.append(value)            # 直接使用栈A完成在栈顶添加即可

    def deleteHead(self) -> int:
        if self.B:              # 如果B不为空，那么证明A的元素全都塞到了B中，B最后一个就是A的head
            return self.B.pop()
        if not self.A:
            return -1       # 为空返回-1
        while self.A:
            self.B.append(self.A.pop())     # 将A中的元素全都塞到B中
        return self.B.pop()





