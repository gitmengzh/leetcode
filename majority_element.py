'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1:
输入: [3,2,3]
输出: 3
示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2
'''

def majorityElement(nums):
    new_nums = set(nums)
    new_dict = {}
    for i in new_nums:
        new_dict.update({i:0})
    for j in nums:
        if j in new_dict.keys():
            new_value = new_dict.get(j)+1
            new_dict.update({j:new_value})
    res = []
    for s in new_dict.keys():
        if new_dict.get(s)>len(nums)/2:
            res.append(s)
    return res
def majorityElement2(nums):
    nums.sort()
    return nums[len(nums)//2]





if __name__ == "__main__":
    nums = [1,2,3,3,4,5,5,5,5,5,5]
    print(majorityElement2(nums))