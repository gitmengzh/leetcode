'''
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
示例 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
'''

# 使用sorted函数
def squares_of_a_sorted_array(A):
    j = 0
    for i in A:
        A[j] = i**2
        j+=1
    return sorted(A)
    # 优化
    # return sorted([num*num for num in A])

# 提交后，超时了
def squares_of_a_sorted_array2(A):
    j = 0
    for i in A:
        A[j] = i**2
        j+=1
    for k in range(len(A)):
        for z in range(0, len(A) - k - 1):
            if A[z] > A[z + 1]:
                    A[z], A[z + 1] = A[z + 1], A[z]

    return A



if __name__ == "__main__":
    a1 = [-4,-1,0,3,10]
    a2 = [-7,-3,2,3,11]
    print(squares_of_a_sorted_array2(a1))
