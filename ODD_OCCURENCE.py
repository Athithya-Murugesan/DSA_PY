def find_odd_occurrence(arr):
    def binary_search_odd(arr, left, right):
        if left > right:
            return None
        
        if left == right:
            return arr[left]
        
        mid = left + (right - left) // 2
        
        # Check if mid is the odd occurring element
        if mid % 2 == 0:
            if arr[mid] == arr[mid + 1]:
                return binary_search_odd(arr, mid + 2, right)
            else:
                return binary_search_odd(arr, left, mid)
        else:
            if arr[mid] == arr[mid - 1]:
                return binary_search_odd(arr, mid + 1, right)
            else:
                return binary_search_odd(arr, left, mid - 1)
    
    return binary_search_odd(arr, 0, len(arr) - 1)

# Example 1
n=int(input())
list = list(map(int,input().split()))
print(find_odd_occurrence(list))


