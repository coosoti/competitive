class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_p, above_p, p = [], [], []
        for i in range(len(nums)):
            if nums[i] < pivot:
                less_p.append(nums[i])
            elif nums[i] > pivot:
                above_p.append(nums[i])
            else:
                p.append(nums[i])
        return less_p + p + above_p