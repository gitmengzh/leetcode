'''
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
'''
def removeDuplicates1(nums):
    new_list = []
    for i in nums:
        if i not in new_list:
            new_list.append(i)
    for i in range(len(new_list)):
        nums[i] = new_list[i]
    return len(new_list), nums

# 三种方法中效率最低
def removeDuplicates2(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] not in nums[:i]:
            nums[count] = nums[i]
            count += 1
    return count


#双指针
def removeDuplicates3(nums):
    a = 0
    b = 1
    while b < len(nums):
        if nums[b] == nums[a]:
            b += 1
        else:
            a += 1
            nums[a] = nums[b]
    return a + 1

nums = [0,0,0,1,2,3,4,2,3]
nums2 = [-1,0,0,0,0,3,3]
nums3 = [1,1,2]
# print(removeDuplicates(nums2))
# removeDuplicates(nums)
print(nums[:0])


'''
关于双指针，有两种情况
1 相同方向的两个指针（快慢指针）
    快慢指针也是双指针，但是两个指针从同一侧开始遍历数组，
    将这两个指针分别定义为快指针（fast）和慢指针（slow），
    两个指针以不同的策略移动，直到两个指针的值相等（或其他特殊条件）为止，
    如fast每次增长两个，slow每次增长一个。
2 相对方向的两个指针（对撞指针）
    对撞指针是指在有序数组中，将指向最左侧的索引定义为左指针(left)，
    最右侧的定义为右指针(right)，然后从两头向中间进行数组遍历。
    对撞数组适用于有序数组，也就是说当你遇到题目给定有序数组时，应该第一时间想到用对撞指针解题。

'''