import time
import random

def find_el(el_to_find, arr):

    for i in arr:
        if i == el_to_find:
            return True
    return False



def second_max(arr):
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    for i in arr[2:]:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
    return max2

def find_el_binary(el_to_find, arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == el_to_find:
            return True
        elif arr[mid] < el_to_find:
            left = mid + 1
        else:
            right = mid - 1
    return False


def table_create(size):
    table = []
    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            row.append(i * j)
        table.append(row)

    return table



def time_count_one_arg(func, arg1):
    start = time.perf_counter()
    func(arg1)
    end = time.perf_counter()
    return f"{(end - start):.8f}"

def time_count_two_args(func, arg1, arg2):
    start = time.perf_counter()
    func(arg1, arg2)
    end = time.perf_counter()
    return f"{(end - start):.8f}"


def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr



if __name__ == "__main__":
    print("n       el        second_max       find_el     find_el_binary     create_table")
    sizes = [100, 1000, 5000, 10000]
    for i in sizes:
        arr = generate_array(i)
        sorted_arr = sorted(arr)
        el = random.randint(0, i)
        t1 = time_count_one_arg(second_max, arr)
        t2 = time_count_two_args(find_el, el, arr)
        t3 = time_count_two_args(find_el_binary, el, sorted_arr)
        t4 = time_count_one_arg(table_create, el)
        print(i, el, t1, t2, t3, t4, sep="     ")





