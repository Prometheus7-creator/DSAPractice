from collections import Counter
# Naive
# Time - O(n)
# Space - O(n)
# def element_appearing_once(arr, n):
    
#     frequency = Counter(arr)
    
#     for key, val in frequency.items():
        
#         if val == 1:
#             return key


# Optimal - 1
# Time - O(n)
# Space - O(1)

# since the input array is sorted 
# we can check if an element is not equal to the next element
# skip otherwise
# def element_appearing_once(arr, n):
    
#     i = 0
    
#     while i < n-1:
        
#         if arr[i]!=arr[i+1]:
#             return arr[i]
#         else:
#             i += 1
        
#         i += 1
    

# Optimal - 2
# Time - O(n)
# Space - O(1)

def element_appearing_once(arr, n):
    
    ans = 0
    
    for i in arr:
        
        ans ^= i
        
    return ans




if __name__=='__main__':
    
    testcases = int(input('Enter number of testcases: '))
    
    for i in range(testcases):
        n = int(input('Enter size of the array: '))
        arr = list(map(int, input('Enter the elements of array: ').split()))
        
        print(element_appearing_once(arr, n))
