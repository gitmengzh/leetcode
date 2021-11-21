"""

"""

def  wateringPlants(plants, capacity):
    res = 1
    if len(plants) == 1:
        return res
    cout = 1
    mark = 0
    ban = capacity - plants[0]
    for i in range(1, len(plants)):
        cout += 1
        if ban > plants[i]:
            if mark == 1:
                res += (2*cout-1)
                ban -= plants[i]
            else:
                ban -= plants[i]
                res += 1
            mark = 0

        elif plants[i] == ban:

            if i != len(plants)-1:
                # if mark == 0:
                #     ban = capacity
                #     res += 1
                # else:
                #     ban = capacity
                #     res += 2 * cout -1
                # mark = 1
                res+=1
            else:
                # res+=2 * cout -1
        else:
            # if mark == 1:
            #     if i == (len(plants)-1):
            #         res += (2*cout-1)
            #     else:
            #         ban = capacity
            #         res+=(2*cout-1)
            # else:
            if i == (len(plants)-1):
                res += (2*cout-1)
            else:
                ban = capacity
                res += (2*cout-1)
                ban -= plants[i]

            mark = 1

    return res

if __name__ == "__main__":
    plants1 = [2,2,3,3]
    capacity1 = 5
    plants2 = [1,1,1,4,2,3]
    capacity2 = 4
    plants3 = [7, 7, 7, 7, 7, 7, 7]
    capacity3 = 8
    plants4 = [4, 4, 4, 4, 4, 4]
    plants5 = [1, 1, 1, 1, 4, 4, 1, 3, 4]
    capacity4 = 4
    capacity5 = 4
    plants6 = [3, 2, 4, 2, 1]
    capacity6 = 6
    print(wateringPlants(plants6, capacity6))
