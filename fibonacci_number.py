'''
斐波那契数
f(0) = 0
f(1) = 1
之后每一项等于前一项之和
返回第n项
'''

# 递归方法 慢
def fibonacci_number1(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_number1(n-1)+fibonacci_number1(n-2)

# 数学方法
def fibonacci_number2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

if __name__ == "__main__":
    n = 10
    print(fibonacci_number1(40))

