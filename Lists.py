if __name__ == '__main__':
    # Initialize an empty list
    my_list = []

    # Read the number of commands
    N = int(input())

    # Iterate through each command
    for _ in range(N):
        # Read the command
        command = input().split()

        # Implement list inbuilt functions as commands
        if command[0] == 'insert':
            # Implement command: insert i e
            my_list.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            # Implement command: print
            print(my_list)
        elif command[0] == 'remove':
            # Implement command: remove e
            my_list.remove(int(command[1]))
        elif command[0] == 'append':
            # Implement command: append e
            my_list.append(int(command[1]))
        elif command[0] == 'sort':
            # Implement command: sort
            my_list.sort()
        elif command[0] == 'pop':
            # Implement command: pop
            my_list.pop()
        elif command[0] == 'reverse':
            # Implement command: reverse
            my_list.reverse()