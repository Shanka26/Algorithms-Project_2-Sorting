def sort(arr):
    if len(arr) > 1:
  
        # Find middle of array
        mid = len(arr)//2
  
        # Divide array intotwo half
        L = arr[:mid]
        R = arr[mid:]
  
        # Sort the first half
        sort(L)
        # Sort the second half
        sort(R)

        # innit iterators
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            # Add lowest value to original array
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Check if any element is left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

ar=[9,2,6,8,2,5,4,7,1,4,8,4,5]
print(ar)
sort(ar)
print(ar)