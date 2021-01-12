# 快速排序


def aaa(arr, low, high):
    i = low
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickSort(arr, low, high):
    if low < high:
        res = aaa(arr,low, high)
        quickSort(arr, low, res-1)
        quickSort(arr, res+1, high)
    return arr

if __name__ == "__main__":
    arr = [10, 22, 78, 3, 12, 9, 1, 11, 33, 2]
    low = 0
    high = len(arr)-1
    print(quickSort(arr, low, high))