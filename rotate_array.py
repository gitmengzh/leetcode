'''
旋转数组

'''
# 本题要注意看>len(nums)的情况
def rotate_array(nums,k):
    # nums = nums[-k:]+nums[:-k]
    # 切片方法
    # nums[] = nums[len(nums)-k:]+nums[:k-len(nums)]
    # 循环方法
    for i in range(k):
        val = nums.pop()
        nums.insert(0,val)

    return nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 8
    print(rotate_array(nums,k))