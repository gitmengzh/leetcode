"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

说明：
    输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
    我们可以不考虑输出结果的顺序。

进阶：
    如果给定的数组已经排好序呢？你将如何优化你的算法？
    如果 nums1 的大小比 nums2 小很多，哪种方法更优？
    如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
"""
import collections

def intersect(nums1, nums2):
    res = []
    if len(nums1) < len(nums2):
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])
                nums2.remove(nums1[i])
    else:
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                res.append(nums2[j])
                nums1.remove(nums2[j])
    return res

def intersect2(nums1, nums2):       #  hashmap  collection.Counter
    count1 = collections.Counter(nums1)
    count2 = collections.Counter(nums2)
    res = []
    if len(count1.keys()) < len(count2.keys()):
        for i in count1.keys():
            if i in count2.keys():
                for j in range(min(count1[i], count2[i])):
                    res.append(i)
    else:
        for i in count2.keys():
            if i in count1.keys():
                for j in range(min(count1[i], count2[i])):
                    res.append(i)
    return res

def intersect3(nums1, nums2):   # 排序+双指针
    l1 = len(nums1)
    l2 = len(nums2)
    nums1.sort()
    nums2.sort()
    i = j = 0
    res = []
    while i <l1 and j < l2:
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1
    return res
if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    nums3 = [4, 9, 5]
    nums4 = [9, 4, 9, 8, 4]
    print(intersect3(nums1, nums2))
