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


class RangeCounts:
    def __init__(self, expenditure, d):
        # since each value of expenditure can go from 0 to 200, we can make a bucket of 201 counts
        self.d = d
        # self.sorted_expenses = [-1]*d

        self.counts = [0]*201
        for i in range(d):
            self.counts[expenditure[i]] += 1

        # j = 0
        # for expense in range(len(self.counts)):
        #     count = self.counts[expense]
        #     while count > 0:
        #         self.sorted_expenses[j] = expense
        #         j += 1
        #         count -= 1

    def remove(self, expense):
        self.counts[expense] -= 1
        # self.sorted_expenses.remove(expense)

    def add(self, expense):
        # print("adding ", expense)
        self.counts[expense] += 1
        # self.sorted_expenses.append(expense)
        # # insertion sort to put expense in the right position
        # j = len(self.sorted_expenses) - 2
        # while j >= 0 and self.sorted_expenses[j] > expense:
        #     self.sorted_expenses[j+1] = self.sorted_expenses[j]
        # self.sorted_expenses[j+1] = expense

    def median(self):
        # print("finding median")
        is_odd = self.d & 1 == 1
        middle_high = self.d//2 + 1
        middle_low = middle_high-1
        median_low = -1
        median_high = -1
        # print("middle_low: ", middle_low, "middle_high: ", middle_high)
        # print("is_odd", is_odd)

        c = 0
        for i in range(len(self.counts)):
            c += self.counts[i]
            if c >= middle_low and median_low == -1:
                median_low = i

            if c >= middle_high:
                median_high = i
                break
        if is_odd:
            return median_high
        else:
            return (median_low+median_high)/2


def activityNotifications(expenditure, d):
    notifications = 0
    expenses = RangeCounts(expenditure, d)
    for i in range(d, len(expenditure)):
        # print(expenses.counts)
        current_median = expenses.median()
        # print(current_median)
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
