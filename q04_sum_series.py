def m_series(i):
    result = 0.0
    for i in range(1, i+1):
        result += (i / (i+1))
    return result

maximum = int(input('Enter number: '))
print("{0:10}m(i)".format("i"))
for a in range(1, maximum+1):
    print("{0:<10}{1:.4f}".format(a, m_series(a)))

