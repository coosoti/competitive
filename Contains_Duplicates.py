class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_nums = set(nums) # after removing the duplicates
        if len(nums) != len(new_nums):
            return True
        return False