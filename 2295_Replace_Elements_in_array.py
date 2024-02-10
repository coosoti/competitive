class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # A dictionary to store the mappings of numbers
        num_map = {nums[i]: i for i in range(len(nums))}

        # Now iterating through the operations
        for operation in operations:
            old, new = operation

            # next, replace old with new in nums array
            nums[num_map[old]] = new

            # then, update the num_map dictionary
            num_map[new] = num_map.pop(old)
    
        return nums