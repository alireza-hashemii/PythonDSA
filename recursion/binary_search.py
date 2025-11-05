def binary_search(data, target, low , high):
    mid = (low + high) // 2

    if low > high:
       return 'Not Found'
    
    else:
        if data[mid] == target:
            return f"Found The Item at {mid}"
        
        elif data[mid] > target:
            return binary_search(data, target, low, mid - 1)
        elif data[mid] < target:
            return binary_search(data, target, mid + 1, high)
    

result = binary_search([2, 4, 5, 6, 8, 12, 15, 18], 18, 0, 7 )
print(result)