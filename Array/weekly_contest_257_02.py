# url: https://leetcode-cn.com/contest/weekly-contest-257/problems/the-number-of-weak-characters-in-the-game/

def numberOfWeakCharacters(propertie):
    res = 0
    temp = []
    for i in range(len(propertie)):
        if i not in temp :
            for j in range(i, len(propertie)):
                if j not in temp:
                    if propertie[i][0] < propertie[j][0] and propertie[i][1] < propertie[j][1]:
                    # if j not in temp:
                        res += 1
                        i += 1
                        break
                    elif propertie[i][0] > propertie[j][0] and propertie[i][1] > propertie[j][1]:
                        res += 1
                        temp.append(j)


    return res

def numberOfWeakCharacters2(properties):
    # 相同攻击力时按照防御降序排列
    properties.sort(key=lambda x: (x[0], -x[1]))  # 根据第一个元素进行排序，如果第一个元素相同，那么根据第二个元素的负数进行排序，从小到大

    v = list(t[1] for t in properties)

    # 单调栈判断是否存在比当前元素大的数
    ans = 0
    stack = []
    for i in range(len(v)):
        if not stack:
            stack.append(v[i])
        else:
            if stack[-1] >= v[i]:
                stack.append(v[i])
            else:
                while stack and stack[-1] < v[i]:
                    stack.pop(-1)
                    ans += 1
                stack.append(v[i])
    return ans


if __name__ == "__main__":
    properties = [[5,5],[6,3],[3,6]]
    properties1 = [[2, 2], [3, 3]]
    properties2 = [[5, 5], [3, 5], [6,6],[3,3], [4,4],[7,6]]
    properties3 = [[3,3], [2,2], [1,1]]
    properties4 = [[7, 7], [1, 2], [9, 7], [7, 3], [3, 10], [9, 8], [8, 10], [4, 3], [1, 5], [1, 5]]
    properties5 = [[3, 3], [2, 2], [4,4]]
    # print(numberOfWeakCharacters2(properties4))
    properties6 = [[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
    properties6.sort(key=lambda x: (x[0], -x[1]))
    print(properties6)