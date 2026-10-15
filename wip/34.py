"""34"""

def int_to_list(i: int) -> list:
    """145 -> [1,4,5]"""
    ints = []
    while True:
        # print(i)
        if i < 10:
            ints = [i] + ints
            break

        ints = [i % 10] + ints
        i = int(i / 10)

    return ints


def factorial(i: int) -> int:
    if i < 3:
        return i

    result = 1
    for i in range(2, i + 1):
        result *= i
    return result


def main():
    search_length: int = 100000
    # results: list = []

    for i in range(3, search_length):
        ints = int_to_list(i)

        sum_of_factorials = 0
        for j in ints:
            sum_of_factorials += factorial(j)

        if sum_of_factorials == i:
            print(f"Found int equal to sum of factorials: {i}")


if __name__ == "__main__":
    main()
