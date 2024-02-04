class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #For easier implementation, we sort the list of strings
        strs.sort()
        prefix = ""
        for i in range(len(strs[0])):
            #since they are sorted lexicographically we compare the prefixes in 
            ###first and last strings in the array
            if strs[0][i] == strs[-1][i]:
                prefix += strs[0][i]
            else:
                break
        return prefix

        
