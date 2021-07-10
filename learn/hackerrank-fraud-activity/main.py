import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#


def partition(arr, pivot_index, low, high):
    pivot = arr[pivot_index]

    # all the elements left to i are smaller than pivot
    i = low
    j = low
    while j <= high:
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            if i == pivot_index:
                i += 1
        j += 1
        if j == pivot_index:
            j += 1

    if pivot_index < i:
        arr[i-1], arr[pivot_index] = arr[pivot_index], arr[i-1]
        return i-1
    else:
        arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
        return i


def move_pos(arr, pos, low, high):
    while True:
        got_pos = partition(arr, low, low, high)
        if got_pos == pos:
            return
        elif got_pos < pos:
            low = got_pos+1
        else:
            high = got_pos-1


def median(arr, low, high):
    length = (high+1)-low
    is_odd = length & 1 == 1
    if is_odd:
        median_index = low+(length//2)
        move_pos(arr, median_index, low, high)
        return arr[median_index]
    else:
        upper_median_index = low+(length//2)
        lower_median_index = upper_median_index - 1
        move_pos(arr, lower_median_index, low, high)
        move_pos(arr, upper_median_index, low, high)
        return (arr[lower_median_index] + arr[upper_median_index])/2


class RangeCounts:
    def __init__(self, expenditure, d):
        # since each value of expenditure can go from 0 to 200, we can make a bucket of 201 counts
        self.d = d
        self.sorted_expenses = [-1]*d

        self.counts = [0]*201
        for i in range(d):
            self.counts[expenditure[i]] += 1

        j = 0
        for expense in range(len(self.counts)):
            count = self.counts[expense]
            while count > 0:
                self.sorted_expenses[j] = expense
                j += 1
                count -= 1

    def remove(self, expense):
        self.counts[expense] -= 1
        self.sorted_expenses.remove(expense)

    def add(self, expense):
        self.counts[expense] += 1
        self.sorted_expenses.append(expense)
        # insertion sort to put expense in the right position
        j = len(self.sorted_expenses) - 2
        while j >= 0 and self.sorted_expenses[j] > expense:
            self.sorted_expenses[j+1] = self.sorted_expenses[j]
        self.sorted_expenses[j+1] = expense

    def median(self):
        is_odd = self.d & 1 == 1
        if is_odd:
            return self.sorted_expenses[self.d//2]
        else:
            return (self.sorted_expenses[(self.d//2)-1] + self.sorted_expenses[self.d//2])/2


def activityNotifications(expenditure, d):
    notifications = 0
    expenses = RangeCounts(expenditure, d)
    low = 0
    high = d-1
    for i in range(d, len(expenditure)):
        print(expenses.sorted_expenses)
        current_median = expenses.median()
        if expenditure[i] >= 2*current_median:
            notifications += 1
        expenses.add(expenditure[i])
        expenses.remove(expenditure[i-d])
    return notifications


if __name__ == '__main__':
    first_multiple_input = sys.stdin.readline().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, sys.stdin.readline().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')
