def create_unique_file_names(n, file_names):
    existing_names = set()
    result = []
    
    for name in file_names:
        if name not in existing_names:
            existing_names.add(name)
            result.append("OK")
        else:
            i = 1
            while f"{name}{i}" in existing_names:
                i += 1
            existing_names.add(f"{name}{i}")
            result.append(f"{name}{i}")
    
    return result

# Example usage:
n = int(input())
file_names = [input() for _ in range(n)]
output = create_unique_file_names(n, file_names)
for name in output:
    print(name)
