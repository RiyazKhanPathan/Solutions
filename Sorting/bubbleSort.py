
# Worst Case: Time O(n2), Space O(1)
def bubbleSort(array):
    
    for i in range(len(array)):
        swapped = False # to handle the case with sorted array
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] =  array[j+1], array[j]
                swapped = True
            
        # no swapping means the array is already sorted
        if not swapped:
            break

    return data


data = [-2, 45, 0, 11, -9]


print(bubbleSort(data))