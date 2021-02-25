# 冒泡排序  从小到大

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == "__main__":
    arr1 = [1,3,2,5]
    arr2 = [3,4,2,5,3,2,1]
    arr3 = [1, 6, 7, 2, 9, 4]
    print(bubbleSort(arr3))