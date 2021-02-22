

def search_range (nums,target):
    low=0
    hight=len(nums)-1
    while low <= hight:
        mid=low+(hight-low)//2
        if target < nums[mid]:
            hight = mid-1
        if target > nums[mid]:
            low=mid+1
        else:
            break

    for j in range(len(nums)-1,-1,-1):
        if nums[j]==target:
            return [mid ,j]
    
    return[None,None]


print(search_range([5,7,7,8,8,8,10],10))