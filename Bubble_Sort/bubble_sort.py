def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements of the array
    for i in range(n):
        # Flag to check if a swap was made in this iteration
        swapped = False
        
        # Last i elements are already sorted, so we ignore them
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if the element is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no elements were swapped, the list is already sorted
        if not swapped:
            break

    return arr

# Test the bubble sort function
arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
