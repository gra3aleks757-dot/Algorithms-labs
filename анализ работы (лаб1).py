import random
import time
import sys

def generate_array(n):
    return [random.randint(0, 10000) for _ in range(n)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def measure_time_sort(sort_func, arr):
    arr_copy = arr.copy()
    start = time.perf_counter()
    sort_func(arr_copy)
    end = time.perf_counter()
    return end - start


def measure_space_sort(sort_func, arr):
    arr_copy = arr.copy()
    
    
    memory_before = sys.getsizeof(arr_copy)
    for item in arr_copy:
        memory_before += sys.getsizeof(item)
    
    
    sort_func(arr_copy)
    
   
    memory_after = sys.getsizeof(arr_copy)
    for item in arr_copy:
        memory_after += sys.getsizeof(item)
    
    return memory_after - memory_before

" Запуск эксперимента"
if __name__ == "__main__":
    
    sizes = [100, 500, 1000, 2000, 3000] 
    
    print("Эксперимент с сортировкой пузырьком")
    print("-" * 50)
    print(f"{'Размер (n)':<12} {'Время (сек)':<20} {'Память (байт)':<20}")
    print("-" * 50)
    
    for n in sizes:
        
        arr = generate_array(n)
        
       
        time_taken = measure_time_sort(bubble_sort, arr)
        
        
        memory_used = measure_space_sort(bubble_sort, arr)
        
        
        print(f"{n:<12} {time_taken:<20.6f} {memory_used:<20}")
