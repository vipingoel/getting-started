import sys

# Write your code here
if __name__ == "__main__":
    x = int(sys.stdin.readline())
    count = 0
    while x > 0:
        if x & 1:
            count += 1
        x >>= 1
    print(count)
