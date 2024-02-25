class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1, n + 1)]
        j = 0
        while len(nums) > 1:
            j += k - 1
            temp = len(nums)
            nums.pop(j % temp)
            j = j % temp
        return nums[0]