import sys
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

if __name__ == "__main__":
    input_lines = sys.stdin.readlines()
    n = int(input_lines[0])
    arr = list(map(int, input_lines[1].split()))
    positions = {arr[i]: i for i in range(n)}

    # do insertion sort
    for i in range(n):
        # for each element in array
        # check on the left and move the current element to correct position
        inserting_element = arr[i]
        j = i-1
        while j >= 0 and arr[j] > inserting_element:
            arr[j+1] = arr[j]
            positions[arr[j]] = j+1
            j = j-1
        arr[j+1] = inserting_element
        positions[inserting_element] = j+1
        # print("arr")
        # for a in arr:
        #     print(f'{a:03}', end=" ")
        # print("\npositions")
        # for p in positions:
        #     print(f'{p:03}', end=" ")
        # print("\n-------------------------------------------------------------------------")

    for val in positions.values():
        print(val+1, end=" ")
