import functions

def insertion_sort(array):
    if len(array) <= 1:
        return array
    
    n = len(array)
    for i in range(1, n):
        x = array[i]
        j = i
        
        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1
        
        array[j] = x
    
    return array

if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10000]
    
    for i in sizes:
        arr = functions.generate_array(i)
        t = functions.time_count_one_arg(insertion_sort, arr.copy())
        print(f"{i:<16} {t}")
