#!/usb/bin/env python3

def main():
    n = int(input()) # Read the number of words

    # Process each word
    for _ in range(n):
        word = input() # Read the word
    
        # Check if the word is too long
        if len(word) > 10:
            # Replace the word with its abbreviation
            abbreviation = word[0] + str(len(word) - 2) + word[-1]
            print(abbreviation)
        else:
            # Print the word as it is
            print(word)
main()