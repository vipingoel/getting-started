import sys


def merge_sort(arr, l, r):
    if l > r:
        raise Exception("left must not be greater than right")

    if l == r:
        # print("[arr[l]]", [arr[l]])
        return [arr[l]]

    m = (l+r)//2
    merge_sort(arr, l, m)
    merge_sort(arr, m+1, r)
    # merged = []
    # merge left and right
    l_start = l
    l_end = m
    r_start = m+1
    r_end = r

    while l_start <= l_end and r_start <= r_end:


        # while left < len(left_sorted) and right < len(right_sorted):
        #     if left_sorted[left] <= right_sorted[right]:
        #         merged.append(left_sorted[left])
        #         left += 1
        #     else:
        #         merged.append(right_sorted[right])
        #         right += 1
        # else:
        #     if left == len(left_sorted):
        #         merged += right_sorted[right:]
        #     else:
        # #         merged += left_sorted[left:]
        # print("l, r", l, r)
        # print("merged", merged)
        # return merged
        # program to merge sort an array
if __name__ == "__main__":
    input_lines = sys.stdin.readlines()
    arr = list(map(int, input_lines[0].split()))
    print(merge_sort(arr, 0, len(arr)-1))
