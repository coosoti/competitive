class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_nums = []
        n = len(nums)

        half= len(nums) // 2

        for i in range(half):
            new_nums.append(nums[i])
            new_nums.append(nums[i + half])

        return new_nums
        