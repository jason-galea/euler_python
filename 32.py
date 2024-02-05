#!/usr/bin/python3


def digitize(n, base=10):
    if n == 0:
        yield 0
    while n:
        n, d = divmod(n, base)
        yield d


def is_pandigital(i):
    if i == 1: return True

    i_list = list(digitize(i))
    i_len = len(i_list)
    i_set = set(i_list)

    return i_set == set(range(1, i_len + 1 )) ### E.G: {3,1,2} == {1,2,3}


def main_single_integers():
    LIMIT = 10000

    for i in range(LIMIT):
        if is_pandigital(i):
            print(f"Success with i = {i}")


def main():
    pass


if __name__ == "__main__":
    # main()
    main_single_integers()
