from collections import Counter

def count_pairs(N, a, b, c):
    count_b = Counter(b)
    count_c = Counter(c)
    total_pairs = 0

    for ai in a:
        total_pairs += count_b[ai] * count_c[ai]

    return total_pairs

if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    print(count_pairs(N, a, b, c))
