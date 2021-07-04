import sys
import random


def partition_first(arr, low, high):
    pivot = arr[low]
    i = low+1
    for j in range(low+1, high+1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        # print(arr)
    i -= 1
    arr[low], arr[i] = arr[i], arr[low]
    return i


def partition_last(arr, low, high):
    pivot = arr[high]
    i = low
    # low to high-1
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[high], arr[i] = arr[i], arr[high]
    return i


def partition_random(arr, low, high):
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    i = low
    # low to high-1
    for j in range(low, pivot_index):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    for j in range(pivot_index+1, high+1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            # skip the replacement for pivot element
            if i == pivot_index:
                i += 1

    if i > pivot_index:
        i -= 1

    arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
    return i


def quick_sort(arr, low, high):
    if low >= high:
        return

    pos = partition_random(arr, low, high)
    quick_sort(arr, low, pos-1)
    quick_sort(arr, pos+1, high)


if __name__ == "__main__":
    arr = list(map(int, sys.stdin.readline().split()))
    quick_sort(arr, 0, len(arr)-1)
    print(arr)
