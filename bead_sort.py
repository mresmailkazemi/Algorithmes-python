def bead_sort(arr):
    if any(not isinstance (x,int) or x <0 for x in arr):
        return TypeErroe (' arr must be list od not-negative integers ')
    
    for _ in range(len(arr)):
        for i,(rod_upper,rod_lower) in enumerate(zip(arr,arr[1:])):
            if rod_upper > rod_lower:
                arr[i] -= rod_upper- rod_lower
                arr[i+1] += rod_upper- rod_lower
    return arr


print(bead_sort([1,4,2,6,7,8,1,3]))