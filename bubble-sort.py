#! /usr/bin/env Python
# Bubble sort is a sorting method.

# You will iterate through the array multiple times until you have the array in ascending order
print("*********************************")
print("*    Starting bubble sorting    *")
print("*********************************\n\n")

def sort(nums):
    for i in range(len(nums) -1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                # temp = nums[j]
                # nums[j] = nums[j+1]
                # nums[j+1] = temp
                nums[j],nums[j+1] = nums[j+1],nums[j]

nums = [-1, 9, 9.1, -9.3, 7, 3]
print(f"given list:\n{nums}")
sort(nums)
print(f"Results: \n{nums}")