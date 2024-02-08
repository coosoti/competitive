def main():
    # Read the number of test cases
    t = int(input())

    # Iterate through each test case
    for _ in range(t):
        # Read the input string and convert it to lowercase
        s = input().strip().lower()
        
        # Get the length of the input string
        size = len(s)
        
        # Initialize counts for characters with even occurrences, odd occurrences, and single occurrences
        even_count, odd_count, single_count = 0, 0, 0
        
        # Count the occurrences of each letter in the input string
        letter_counts = {}
        for char in s:
            if char.isalpha():
                letter_counts[char] = letter_counts.get(char, 0) + 1

        # Count the types of occurrences: even, odd, and single
        for count in letter_counts.values():
            if count % 2 == 0 and count != 0:
                even_count += 1
            elif count % 2 != 0 and count != 0 and count != 1:
                odd_count += 1
            elif count == 1:
                single_count += 1

        # Check the conditions for rearranging letters to form another palindrome
        if size <= 3 or even_count + odd_count == 1 or even_count * single_count == 1:
            # If conditions are met, print NO
            print("NO")
        else:
            # Otherwise, print YES
            print("YES")

if __name__ == "__main__":
    main()




