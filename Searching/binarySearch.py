
def binarySearch (arr, start, end, key):

	# if end >= start:

	# 	mid = start + (end-start) // 2

	# 	if arr[mid] == key:
	# 		return mid

	# 	elif arr[mid] > key:
	# 		return binarySearch(arr, start, mid-1, key)

	# 	else:
	# 		return binarySearch(arr, mid + 1, end, key)

	# else:
	# 	return -1

    while(end>=start):
        mid = (start+end)//2
        if arr[mid]==key:
            return mid
        elif key > arr[mid]:
            start = mid+1
        else:
            end = mid-1
    return -1
        


arr = [ 2, 3, 4, 10, 40 ]
key = 40
index = binarySearch(arr, 0, len(arr)-1, key)

if index != -1:
	print (f"{key} found at {index+1} pos")
else:
	print ("Not Found")
