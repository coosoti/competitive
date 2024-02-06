#!/usb/bin/env Python3

def main():
    # t is number of testcases
    t = int(input())

    # target word for comparison
    word = "codeforces"

    # Iterate of each testcase
    for _ in range(t):
        s = input() #read each input

        # initial a counter to count all the differences between testcase and word
        diff_count = 0 #initialize at 0

        # Iterate through each ch in the string and compare with word string
        for i in range(len(s)):
            if s[i] != word[i]:
                diff_count += 1
        print(diff_count)
main()
