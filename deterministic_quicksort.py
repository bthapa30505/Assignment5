import random
import time
import tracemalloc
import sys
sys.setrecursionlimit(100001)

def quick_sort(list):
    # Base case: if the list has 0 or 1 elements, it's already sorted
    if len(list) <= 1:
        return list
    else:
        # Select a pivot element (here we choose the last element)
        pivot = list[-1]
        
        # Partition the list into two sublists:
        # - `left` contains elements less than or equal to the pivot
        # - `right` contains elements greater than the pivot
        left = [x for x in list[:-1] if x <= pivot]
        right = [x for x in list[:-1] if x > pivot]
        
        # Recursively sort the sublists and combine them with the pivot
        return quick_sort(left) + [pivot] + quick_sort(right)

def print_difference(start_time, end_time, data_type, size):
    print(f"Time taken for {data_type} (size {size}): {end_time - start_time:.6f} seconds")

def measure_memory_quick_sort(arr, data_type, size):
    tracemalloc.start() 
    quick_sort(arr)
    current, peak = tracemalloc.get_traced_memory() 
    tracemalloc.stop()
    print(f"Quick Sort: {data_type} (size {size}) - Current memory usage: {current / 1024:.2f}KB; Peak memory usage: {peak / 1024:.2f}KB")

def test_quicksort(size):
    # Generate datasets for the given size
    sorted_data = list(range(1, size + 1))  # Sorted data
    sorted_descending = list(range(size, 0, -1))  # Reverse sorted data
    random_data = random.sample(range(1, size + 1), size)  # Random data (no duplicates)

    # Test sorted data
    start_time = time.time()
    quick_sort(sorted_data)
    end_time = time.time()
    print_difference(start_time, end_time, "sorted data for deterministic quick sort", size)

    # Test reverse sorted data
    start_time = time.time()
    quick_sort(sorted_descending)
    end_time = time.time()
    print_difference(start_time, end_time, "reverse sorted data for deterministic quick sort", size)

    # Test random data
    start_time = time.time()
    quick_sort(random_data)
    end_time = time.time()
    print_difference(start_time, end_time, "random data for deterministic quick sort", size)

    # Measure memory usage for each dataset
    measure_memory_quick_sort(sorted_data, "Deterministic quick sort sorted", size)
    measure_memory_quick_sort(sorted_descending, "Deterministic quick sort reverse sorted", size)
    measure_memory_quick_sort(random_data, "Deterministic quick sort random", size)

# Test with 10,000 numbers
print("Testing with 10,000 numbers:")
test_quicksort(10000)

# Test with 20,000 numbers
print("Testing with 20,000 numbers:")
test_quicksort(20000)