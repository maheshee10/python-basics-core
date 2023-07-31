# bubble sort uses swapping techinque // so far bubble search uses sort list and middle value compariosn tech
# linear search simple checking for elemnt
# swapping - a,b - take temp var - store a in temp- then give b val in a and temp val in b

def bubblesort(lst):
    for i in range(len(lst)-1,0,-1):

        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j+1]=nums[j]
                nums[j+1] =temp




nums = [2,3,6,7,84,34,56,23,45,546,234,456,23]
print(bubblesort(nums))
print(nums)
