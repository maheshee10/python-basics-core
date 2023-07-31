# sel sort we find min value of each iteration // in bubbles sort we check two values and swap until last vbal is fixed at 8
# swap min valuwe with first index -- swapping only once
# bubble sort we sort for various values in each iteration
# for max value we go from highest index to lowest index
# fo min value go from low index to high index
def selsort(nums):
    for i in range(len(nums)-1):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp





nums = [56,67,3,67,345,567,34,576,344,6]
selsort(nums)
print(nums)