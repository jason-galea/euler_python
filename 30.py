#!/usr/bin/python3

def digitize(n, base=10):
    """
    https://stackoverflow.com/questions/1906717/how-to-split-an-integer-into-a-list-of-digits
    """
    if n == 0:
        yield 0
    while n:
        n, d = divmod(n, base)
        yield d


def main():
    LIMIT = 10**6
    TARGET_POWER = 5
    SUCCESS_LIST = []

    print(f"Limit = {LIMIT}")

    for i in range(2, LIMIT):
        i_digits = list(digitize(i))
        i_digits.reverse()

        # print(f"{i=}")
        # print(f"{i_digits=}")

        total_powers_of_i_digits = 0
        for j in i_digits:
            total_powers_of_i_digits += j**TARGET_POWER

        # print(f"{total_powers_of_i_digits=}")

        if i == total_powers_of_i_digits:
            print(f"Success with i = {i}")
            # print(f"{i=}")
            # print(f"{i_digits=}")
            # print(f"{total_powers_of_i_digits=}")
            # print()
            SUCCESS_LIST.append(i)

    print(f"Result = {sum(SUCCESS_LIST)}")


if __name__ == "__main__":
    main()
