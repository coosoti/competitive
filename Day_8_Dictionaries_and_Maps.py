# n is the number of entries in the phone book
n = int(input())

# phone_book is a dictionary
phone_book = {}

# populate the phone book dictionary with contact entries
for _ in range(n):
    entry = input().split()
    name = entry[0]
    phoneNumber = entry[1]
    phone_book[name] = phoneNumber


# We can now process the queries and print the results
while True:
    try:
        q_name = input()
        if q_name in phone_book:
            print(f"{q_name}={phone_book[q_name]}")
        else:
            print("Not found")
    except EOFError: # continue reading lines until there is no more input
        break
