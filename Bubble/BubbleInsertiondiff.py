import time

def print_array(arr, highlight_indices=[]):
    # Print array elements, highlight elements being compared or moved
    output = []
    for i, val in enumerate(arr):
        if i in highlight_indices:
            output.append(f"[{val}]")
        else:
            output.append(str(val))
    print(" ".join(output))

def bubble_sort(arr):
    n = len(arr)
    print("\nBubble Sort Process:")
    for i in range(n):
        for j in range(n - i - 1):
            print_array(arr, [j, j+1])
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"Swapped {arr[j]} and {arr[j+1]}")
            time.sleep(0.5)
    print("Sorted array (Bubble Sort):", arr)

def insertion_sort(arr):
    n = len(arr)
    print("\nInsertion Sort Process:")
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        print_array(arr, [i])
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            print_array(arr, [j, j+1])
            j -= 1
            time.sleep(0.5)
        arr[j + 1] = key
        print(f"Inserted {key} at position {j+1}")
        time.sleep(0.5)
    print("Sorted array (Insertion Sort):", arr)

# Test array
test_array1 = [5, 3, 8, 4, 2]
test_array2 = test_array1.copy()

bubble_sort(test_array1)
insertion_sort(test_array2)
