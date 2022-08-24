# Naive O(sqrt(n))
# def floor_sqrt(x):
    
#     i = 0
    
#     while i*i <= x:
        
#         i += 1
    
#     return i-1

# Optimal O(logn)
def floor_sqrt(x):
    
    left, right = 0, x
    
    while left <= right:
        
        mid = left + (right - left//2)
        
        if mid*mid == x:
            
            return mid
        
        elif mid*mid < x:
            
            left = mid + 1
            ans = mid
        
        else:
            
            right = mid-1
    
    return ans




testcases = int(input('Enter number of testcases: '))

for i in range(testcases):
    x = int(input('Enter value of x: '))

    print(f'Square root of { x }: { floor_sqrt(x) }')
