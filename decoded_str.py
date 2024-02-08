class Solution:
    def freqAlphabets(self, s: str) -> str:
        decoded_string = ""  # Initialize an empty string to store the decoded result
        index = len(s) - 1  # Start decoding from the end of the string

        # Iterate through the encoded string from right to left
        while index >= 0:
            # Check if the current character is a '#' indicating a double-digit number
            if s[index] == "#":
                # Decode the double-digit number and convert it to a corresponding character
                decoded_char = chr(int(s[index - 2:index]) + 96)
                # Move the index back by 2 to skip the digits and the '#' symbol
                index -= 2
            else:
                # Decode the single-digit number and convert it to a corresponding character
                decoded_char = chr(int(s[index]) + 96)

            # Append the decoded character to the decoded string
            decoded_string += decoded_char
            # Move the index to the left
            index -= 1

        # Reverse the decoded string to get the final result
        return decoded_string[::-1]
