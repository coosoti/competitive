class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elem_count = Counter(nums)

        maj_elems = []

        for el, count in elem_count.items():
            if count > len(nums) // 3:
                maj_elems.append(el)
        
        return maj_elems
        