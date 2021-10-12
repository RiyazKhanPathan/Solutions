# Create a max-heap then swap(root,lastNode)
# pop the last element

# Worst Case: Time O(nlogn), Space O(1)

def heapify(data, sizeOfData, i): 
    largest = i       # set largest as root
    left = 2 * i + 1  # left 
    right = 2 * i + 2 # right 
  

    if (left < sizeOfData and data[i] < data[left]): 
        largest = left 
  
    elif (right < sizeOfData and data[largest] < data[right]): 
        largest = right 
  
    # Change root, if needed 
    if (largest != i): 
        data[i],data[largest] = data[largest],data[i]
  
        # Heapify the root. 
        heapify(data, sizeOfData, largest) 
  
 
def heapSort(data): 
    sizeOfData = len(data) 

    for i in range(sizeOfData+1): 
        heapify(data, sizeOfData, sizeOfData-i) 
  
    # Ascending Order

    for i in range(sizeOfData-1,0,-1): 
        data[i], data[0] = data[0], data[i] # swap 
        heapify(data, i, 0)

    # Descending Order

    # for i in range(sizeOfData-1): 
    #     data[i], data[0] = data[0], data[i] 
    #     heapify(data, i, 0)
    
    return data


data = [4, 10, 3, 5, 1]  

print(heapSort(data))