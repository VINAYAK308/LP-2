
def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):

        # Assume current index has minimum value
        min_index = i

        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Print array after each pass
        print(f"Pass {i + 1}: {arr}")

    return arr


def main():
    # Take input from user
    arr = list(map(int, input("Enter elements separated by space: ").split()))

    print("Original Array:", arr)

    # Call selection sort
    sorted_arr = selection_sort(arr)

    print("Sorted Array:", sorted_arr)


main()



# (venv) trushantramdasjadhav@Trushants-MacBook-Air Python % python3 Assignment3\(Selection\).py
# Enter elements separated by space: 24 23 58 34 60
# Original Array: [24, 23, 58, 34, 60]
# Pass 1: [23, 24, 58, 34, 60]
# Pass 2: [23, 24, 58, 34, 60]
# Pass 3: [23, 24, 34, 58, 60]
# Pass 4: [23, 24, 34, 58, 60]
# Pass 5: [23, 24, 34, 58, 60]
# Sorted Array: [23, 24, 34, 58, 60]
# (venv) trushantramdasjadhav@Trushants-MacBook-Air Python % 