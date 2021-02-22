

def binery_search (nums,target):
    low=0
    hight=len(nums)-1
    while low <= hight:
        mid=low+(hight-low)//2
        val=nums[mid]
        if target < val:
            hight = mid-1
        elif target > val:
            low=mid+1
        elif val==target:
            return mid
    return -1
    

print(binery_search([5,7,7,8,8,8,10],7))