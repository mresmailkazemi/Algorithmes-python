

def first_occurrence (nums,target):
    low=0
    hight=len(nums)-1
    while low < hight:
        mid=low+(hight-low)//2
        val=nums[mid]

        if val < target:
            low=mid+1
        else:
            hight=mid

    if nums[low]==target:
        return low

    

print(first_occurrence([5,7,7,8,8,8,10],8))