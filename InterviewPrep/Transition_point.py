# Naive O(n)
# def transition_point(arr, n):
#     try:
#         return arr.index(1)
#     except ValueError:
#         return -1

# Optimal O(logn)
def transition_point(arr, n):
    
    left, right = 0, n-1
    
    while left<=right:
        
        mid = left + (right-left)//2
        if arr[mid] == 1:
            
            if mid==0 or arr[mid-1]==0:
                return mid
            else:
                right = mid
        elif arr[mid]==0:
            left = mid+1
        else:
            right = mid
    
    return -1


arr = [0,0,0,1,1]

print(transition_point(arr, 5))
