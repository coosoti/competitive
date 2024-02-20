if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

# Generate all possible coordinates using list comprehensions
coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

# Print the filtered coordinates in lexicographic increasing order
print([coord for coord in coordinates if sum(coord) != n])