class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r_nums = [0] * n
        pos, neg = 0, 1
        for i in range(n):
            if nums[i] >= 0:
                r_nums[pos] = nums[i]
                pos += 2
            else:
                r_nums[neg] = nums[i]
                neg += 2
        return r_nums
        