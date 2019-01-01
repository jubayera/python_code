def non_repeating(given_string):

    char_count = {}
    
    for c in given_string:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    for c in given_string:
        if char_count[c] == 1:
            return c

    return None

print non_repeating("abcab")
print non_repeating("abab")
print non_repeating("aabbbc")
print non_repeating("aabbdbc")
