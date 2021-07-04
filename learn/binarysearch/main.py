# Program to search for max number in a sorted array
# that is smaller than or equal a given number
import sys


def search(arr, given):
    l = 0
    r = len(arr)-1

    while l <= r:
        m = (l+r)//2
        if given == arr[m]:
            return m
        elif given > arr[m]:
            if m == len(arr)-1 or given < arr[m+1]:
                return m
            l = m+1
        else:
            if m > 0 and given > arr[m-1]:
                return m-1
            r = m-1
    return -1


if __name__ == "__main__":
    arr = list(map(int, sys.stdin.readline().split()))
    given = int(sys.stdin.readline())

    # lets start with a simple binary search
    print(search(arr, given))
