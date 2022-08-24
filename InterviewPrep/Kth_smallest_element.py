from queue import PriorityQueue

# Naive O(n^2)
# def kth_smallest_element(arr, k):
    
#     smallest = -float('inf')
#     for i in range(k):
#         seen = smallest
#         smallest = float('inf')
#         for j in arr:
#             if j > seen:
#                 smallest = min(smallest, j)
    
#     return smallest

# Optimal - 1 O(nlogn)
# def kth_smallest_element(arr, k):
    
#     return sorted(arr)[k-1]

# Optimal - 2 O(n)
def kth_smallest_element(arr, k):
    
    q = PriorityQueue()
    
    for i in arr:
        q.put(i)
    
    for i in range(k-1):
        q.get()
    
    return q.get()






if __name__ == '__main__':
    
    testcases = int(input('Enter number of testcases: '))
    
    for i in range(testcases):
        n = int(input('Enter size of array: '))
        arr = list(map(int, input('Enter array elements: ').split()))
        k = int(input('Enter value of k: '))
    
        print(kth_smallest_element(arr, k))
