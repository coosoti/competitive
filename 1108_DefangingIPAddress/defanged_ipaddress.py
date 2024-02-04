class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_address = "" #defangedIPAddress

        for char in address: #iterate over all the chars in the address
            if char == ".": # check char is a dot
                new_address += "[.]" #replace with "[.]"
            else:
                new_address += char
        
        return new_address #defanged address
        
