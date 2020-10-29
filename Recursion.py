'''
递归练习题
1 求n的阶乘
2 一只青蛙可以一次跳 1 级台阶或一次跳 2 级台阶,例如:
跳上第 1 级台阶只有一种跳法：直接跳 1 级即可。跳上第 2 级台阶
有两种跳法：每次跳 1 级，跳两次；或者一次跳 2 级。
问要跳上第 n 级台阶有多少种跳法？
3  反转二叉树 将左边的二叉树反转成右边的二叉树
4 斐波那契数


https://zhuanlan.zhihu.com/p/105727776
'''


# 递归
class Recursion(object):
    # 斐波那契数
    def fibonacci_number(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n > 1:
            return self.fibonacci_number(n-1)+self.fibonacci_number(n-2)




if __name__ == "__main__":
    recursion = Recursion()
    print(recursion.fibonacci_number(10))
