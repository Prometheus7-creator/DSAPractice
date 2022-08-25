
# Naive O(n^2)

# def index_of_extra_element(n1, n2, arr1, arr2):
    
#     for i,j in enumerate(arr1):
        
#         if j not in arr2:
            
#             return j
    
#     return n2-1

# Optimal O(n)
def index_of_extra_element(n1, n2, arr1, arr2):
    
    if n1<n2:
        n1,n2 = n2,n1
        arr1,arr2 = arr2, arr1
    
    
    for idx, (i, j) in enumerate(zip(arr1, arr2)):
        
        if i != j:
            return idx
            
    return n1-1



if __name__=='__main__':
    
    testcases = int(input('Enter number of testcases: '))
    
    for i in range(testcases):
        n1 = int(input('Enter size of the array1: '))
        n2 = int(input('Enter size of the array2: '))
        arr1 = list(map(int, input('Enter the elements of array1: ').split()))
        arr2 = list(map(int, input('Enter the elements of array2: ').split()))
        
        print(index_of_extra_element(n1, n2, arr1, arr2))
