class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the maximum consecutive ones and the current window size
        max_consecutive_ones = 0
        current_window_size = 0
        
        # Iterate through the list of numbers
        for num in nums:
            # Check if the current number is 1 (indicating a consecutive one)
            if num == 1:
                # Increment the window size
                current_window_size += 1
            else:
                # If the current number is not 1, update the maximum consecutive ones encountered so far
                max_consecutive_ones = max(max_consecutive_ones, current_window_size)
                # Reset the window size
                current_window_size = 0
        
        # Update the maximum consecutive ones encountered so far after iterating through the entire list
        max_consecutive_ones = max(max_consecutive_ones, current_window_size)

        # Return the maximum consecutive ones found
        return max_consecutive_ones

        