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


def int_to_list_str(i: int) -> list:
    """This sucks, but worse than being gross it's slower"""
    return list(int(s) for s in str(i))


def factorial(i: int) -> list:
    if i < 3:
        return i

    result = 1
    for i in range(2, i + 1):
        result *= i
    return result


def main():
    # results: list = []

    ### Pre compute factorials
    factorials = [0] * 10
    for i in range(10):
        factorials[i] = factorial(i)
    # print(factorials)

    for i in range(3, 999_999):     ### NAIVE --> ~3.15 seconds
                                    ### PRECOMP --> ~1.6 seconds
    # for i in range(3, 4_999_999):   ### NAIVE --> ~17.85 seconds
    #                                 ### PRECOMP --> ~9.15 seconds
        ints = int_to_list(i)
        # ints = int_to_list_str(i)
        # print(f"{ints=}")

        sum_of_factorials = 0
        for j in ints:
            # sum_of_factorials += factorial(j)
            sum_of_factorials += factorials[j]
        # print(f"Sum of factorials for digits {i} = {sum_of_factorials}")

        # # if len(ints) == len(str(sum_of_factorials)):
        # #     print(f"{i} has same length of {sum_of_factorials}")

        if sum_of_factorials == i:
            print(f"Found int equal to sum of factorials: {i}")


if __name__ == "__main__":
    main()
