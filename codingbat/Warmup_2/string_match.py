def string_match(a, b):
    len_a = len(str(a))
    len_b = len(str(b))
    count = 0
    for i in range(len_a, len_b):
        if len_a[i] == len_b[i]:
            count = count + 1

    return count

