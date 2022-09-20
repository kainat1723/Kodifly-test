def Solution(arr):
 
    n = len(arr)
 
    # If length of array is even
    if n % 2 == 0:
        z = n // 2
        e = arr[z]
        q = arr[z - 1]
        ans = (e + q) / 2
        return ans
         
    # If length of array is odd
    else:
        z = n // 2
        ans = arr[z]
        return ans

arr1 = [ 1, 3 ]
arr2 = [ 2, 4 ]
 
arr3 = arr1 + arr2
arr3.sort()
 
print("Median of sorted array = ", Solution(arr3))