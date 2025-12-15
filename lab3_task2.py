def can_split(a, k, max_sum):
    count = 1  
    current_sum = 0
    
    for i in a:
        if current_sum + i > max_sum:
            count += 1 
            current_sum = i 
            if count > k:  
                return False
        else:
            current_sum += i
    return True 


def split_array(a, k):
    left=max(a)
    right=sum(a) 
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_split(a, k, mid):
            result = mid 
            right = mid - 1 
        else:
            left = mid + 1  
    return result


n=list(map(int, input().split()))
a=list(map(int, input().split()))
k=n[1]

print(split_array(a, k))