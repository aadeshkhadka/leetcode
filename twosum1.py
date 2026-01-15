class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # dictionary to store number -> index

        for i, num in enumerate(nums):
            needed = target - num  # what number we need to reach target

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i
