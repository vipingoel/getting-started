import sys


def radix_sort(arr):
    max_element = arr[0]
    for i in range(1, len(arr)):
        max_element = max(max_element, arr[i])

    base = 10
    # lsd = 0
    divisor = 1

    while (max_element//divisor) > 0:
        radix_arr = [None]*10

        for element in arr:
            lsd = (element//divisor) % base
            if radix_arr[lsd]:
                radix_arr[lsd].append(element)
            else:
                radix_arr[lsd] = [element]

        # iterate over radix_arr and fill orig arr with current state
        i = 0
        # print("\n", radix_arr)
        for radix_elements in radix_arr:
            if radix_elements:
                for element in radix_elements:
                    arr[i] = element
                    i += 1

        for element in arr:
            print(element, end=" ")
        print()

        # max_element //= divisor
        # print("\n", "max_element", max_element)
        divisor *= base


# Write your code here
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    radix_sort(arr)
