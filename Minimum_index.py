class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        new_dict = {}
        n1 = len(list1)
        n2 = len(list2)
        for i in range(n1):
            for j in range(n2):
                if list1[i] == list2[j]:
                    new_dict[list1[i]] = i + j
        short_lst = []
        for i, j in new_dict.items():
            if j == min(new_dict.values()):
                short_lst.append(i)
        return short_lst