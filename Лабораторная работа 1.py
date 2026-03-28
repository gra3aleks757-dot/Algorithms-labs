import time
import random
import sys

"Задание №1"
def linear(arr,n):
    for x in arr:
        if x == n:
            return True
    return False

"Задание №2"
def find_second_max(arr):
    if len(arr) < 2:
        return None
    
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]
    return max2

"Задание №3"
def binary_search(arr, target):
    
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

"Задание №4"
def multiplication_table(n):
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            table[i][j] = (i + 1) * (j + 1)
    return table


"Доп фунции"
def generate_array(n):
    return [random.randint(0, 10000) for _ in range(n)]

def measure_time(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start
