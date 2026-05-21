def print_number_pattern(n):
    print("Number Pattern:")
    for i in range(1, n + 1):
        row = ' '.join(str(x) for x in range(1, i + 1))
        print(row)