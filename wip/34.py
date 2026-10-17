"""34"""


def int_to_list_str(i: int) -> list:
    """This sucks, but worse than being gross it's slower"""
    return list(int(s) for s in str(i))


def int_to_list_slow_concat(i: int) -> list:
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


def int_to_list_reverse(i: int) -> list:
    """145 -> [1,4,5]"""
    ints = []
    while True:
        # print(i)
        if i < 10:
            ints.append(i)
            # ints = [i] + ints
            break

        ints.append(i % 10)
        # ints = [i % 10] + ints
        i = int(i / 10)

    return ints


def factorial(i: int) -> list:
    if i < 3:
        return i

    result = 1
    for i in range(2, i + 1):
        result *= i
    return result


### TODO - yeild factorial digits
def main():
    # results: list = []

    ### Pre compute factorials
    factorials = [0] * 10
    for i in range(10):
        factorials[i] = factorial(i)
    print(factorials)

    ### DEBUG - track all ints that match length
    digits_from_length_matched_ints = [0] * 10

    # for i in range(1, 10000):
    for i in range(3, 999_999):     ### (5650G) NAIVE --> ~3.15 seconds
                                    ### (5650G) PRECOMP --> ~1.6 seconds
                                    ### (9800X3D) PRECOMP --> ~0.51 seconds
                                    ### INT_LIST_REV --> ~0.38 seconds
    # for i in range(3, 4_999_999):   ### NAIVE --> ~17.85 seconds
    #                                 ### PRECOMP --> ~9.15 seconds

        # ints = int_to_list_slow_concat(i)
        ints = int_to_list_reverse(i)
        sum_of_factorials = 0
        for j in ints:
            sum_of_factorials += factorials[j]
        # print(f"Sum of factorials for digits {i} = {sum_of_factorials}")

        ### DEBUG
        if len(ints) == len(str(sum_of_factorials)):
            # print(f"{i} has same length of {sum_of_factorials}")
            for k in ints:
                digits_from_length_matched_ints[k] += 1


        if sum_of_factorials == i:
            print(f"Found int equal to sum of factorials: {i}")

    ### DEBUG
    # print(f"{digits_from_length_matched_ints=}")
    for k, v in enumerate(digits_from_length_matched_ints):
        print(f"Int '{k}' found in '{v}' numbers which produced factorial sums of equal length")


if __name__ == "__main__":
    main()
