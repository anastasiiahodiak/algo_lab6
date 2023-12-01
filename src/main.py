def build_prefix_table(needle):
    needle_length = len(needle)
    prefix_table = [0] * needle_length
    j = 0
    i = 1
    prefix_table[0] = 0

    while i < needle_length:
        if needle[i] == needle[j]:
            j += 1
            prefix_table[i] = j
            i += 1
        else:
            if j != 0:
                j = prefix_table[j - 1]
            else:
                prefix_table[i] = 0
                i += 1

    return prefix_table

def match(haystack, needle):
    haystack_length = len(haystack)
    needle_length = len(needle)
    indices = []

    prefix_table = build_prefix_table(needle)

    # haystack_pos = x
    # needle_pos = y

    x = y = 0
    while x + needle_length - y <= haystack_length:
        if needle[y] == haystack[x]:
            y += 1
            x += 1

            if y == needle_length:
                indices.append(x - y)
                y = prefix_table[y - 1]
        else:
            if y != 0:
                y = prefix_table[y - 1]
            else:
                x += 1

    return indices

def main():
    haystack = "ababcababcabcabc"
    needle = "abc"
    result = match(haystack, needle)
    print(result)

if __name__ == "__main__":
    main()