def insertion_sort(arr):
    # Traverse through elements in the array
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be inserted in the sorted portion of the array
        j = i - 1  # The last index of the sorted portion

        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift the element to the right
            j -= 1  # Move to the previous element
        
        # Place the key after finding its correct position
        arr[j + 1] = key
    
    return arr


def main():
    # Input array
    arr = [12, 11, 13, 5, 6]
    
    print("Original Array:")
    print(arr)
    
    # Sort the array using insertion sort
    sorted_arr = insertion_sort(arr)
    
    print("\nSorted Array:")
    print(sorted_arr)


if __name__ == "__main__":
    main()
