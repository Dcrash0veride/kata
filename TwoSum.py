"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""

from itertools import combinations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = []
        for i, j in combinations(nums, 2):
            if i + j == target:
                indexes.append(nums.index(i))
                if nums.index(j) not in indexes:
                    indexes.append(nums.index(j))
                elif nums.index(j) == nums.index(i):
                    indexes.append(len(nums) - nums[-1::-1].index(j) - 1)  
                return indexes
       
            
