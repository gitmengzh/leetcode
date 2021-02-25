
def aaa(group, target):
    # if not group:
    #     return False
    # lenth1 = len(group)
    # lenth2 = len(group[0])
    # slow = 0
    # quick = lenth1
    # start = 0
    # end = lenth2
    # while slow < quick:
    #     while start < end:
    #         if target < group[(start+end)//2][(start+end)//2]:
    #             end = lenth2//2
    #         elif target > group[(start+end)//2][(start+end)//2]:
    #             start = lenth2//2
    #         else:
    #             return False
    #     if start == end:
    #         if target < group[lenth1//2][lenth2//2]:
    for i in range(len(new_list)):
        if target in new_list[i]:
            return True
    return False











if __name__ == "__main__":
    new_list = [
[1, 4, 7, 11, 15],
[2, 5, 8, 12, 19],
[3, 6, 9, 16, 22],
[10, 13, 14, 17, 24],
[18, 21, 23, 26, 30]
        ]


    target = 5
    print(aaa(new_list, target))








