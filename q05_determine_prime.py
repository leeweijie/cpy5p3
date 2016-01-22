from math import floor


def is_prime(n):
    d = floor(n/2)
    for a in range(2, d+1):
        if n % a == 0:
            return False
    return True

counter = 0
for i in range(2, 1001):
    if is_prime(i):
        print("{0:<6}".format(i), end="")
        counter += 1
        if counter != 0 and counter % 10 == 0:
            print()

