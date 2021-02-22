

def last_occurrence(nums,target):
    low=0
    hight=len(nums)-1
    while low <= hight:
        mid=low+(hight-low)//2
        if (nums[mid] == target and mid==len(nums)-1) or \
            (nums[mid] == target and nums[mid+1]>target):
            return mid 
        elif (nums[mid] <= target):
             low=mid+1
        else:
            hight=mid-1
           
    
# def last_occurrence(array, query):
#     lo, hi = 0, len(array) - 1
#     while lo <= hi:
#         mid = (hi + lo) // 2
#         if (array[mid] == query and mid == len(array)-1) or \
#            (array[mid] == query and array[mid+1] > query):
#             return mid
#         elif (array[mid] <= query):
#             lo = mid + 1
#         else:
#             hi = mid - 1
    

print(last_occurrence([2,2,2,3,3,3,5],3))