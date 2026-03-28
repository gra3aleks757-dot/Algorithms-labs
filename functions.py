import time
import random

def find_el(el_to_find, arr):

    for i in arr:
        if i == el_to_find:
            return True
    return False



def second_max(arr):
    max1 = arr[0]
    max2 = arr[0]
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
    return max2

def find_el_binary(el_to_find, arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid_el = arr[(left + right) // 2]
        if mid_el == el_to_find:
            return mid_el

        if mid_el < el_to_find:
            left = arr.index(mid_el) + 1
        else:
            right = arr.index(mid_el) - 1

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
    #print(func(arg1, arg2))
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
        el = random.randint(0, i)
        t1 = time_count_one_arg(second_max, arr)
        t2 = time_count_two_args(find_el, el, arr)
        t3 = time_count_two_args(find_el_binary, el, arr)
        t4 = time_count_one_arg(table_create, el)
        print(i, el, t1, t2, t3, t4, sep="     ")





#print(time_count_two_args(find_el_binary, 2, [1, 2, 3, 4, 6, 7, 8]))
#print(time_count_one_arg(table_create, 6))

