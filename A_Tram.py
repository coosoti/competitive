n = int(input())

capacity = 0
cur_passengers = 0


for _ in range(n):
    a, b = map(int, input().split())
    # Update current passengers inside the tram
    cur_passengers = cur_passengers - a + b
    # Update the capacity if needed
    capacity = max(capacity, cur_passengers)

# Output the minimum possible capacity of the tram
print(capacity)