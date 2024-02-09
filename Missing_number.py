class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        targeted_total = (size * (size + 1)) // 2
        actual_total = sum(nums)
        missing_number = targeted_total - actual_total
        return missing_number