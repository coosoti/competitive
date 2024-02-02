def swap_case(s):
    s = list(s)
    new_s = ''.join([c.upper() if c.islower() else c.lower() for c in s])
    return new_s
