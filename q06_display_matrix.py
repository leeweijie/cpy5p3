from random import randrange


def print_matrix(n):
    for j in range(n):
        for i in range(n):
            print("{0} ".format(randrange(0,2)), end="")
        print()

print_matrix(10)
