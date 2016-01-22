def display_pattern(n):
    # Iterate through the rows
    for i in range(1, n+1):
        row = ""
        # Iterate through the columns
        for j in reversed(range(1, i+1)):
            row += str(j)+" "
        if n >= 10:
            long_number = n-9
        row_width = (n-long_number)+2*long_number+n
        print("{0:>{1}}".format(row,row_width))

display_pattern(20)
