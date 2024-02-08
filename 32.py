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


def get_all_combinations(n):
    result = set()
    complete_set = list(range(1, n + 1)) ### [1, 2, 3]

    for i in complete_set:
        subset_1 = [] ### [?, ?, ?]
        subset_1.append(i) ### [1, ?, ?]
        print(f"{subset_1=}")

        # if...

        ########################### TODO: Reduce set size with each iteration

        for j in subset_1:
            subset_2 = subset_1 ### [1, ?, ?]
            subset_2.append(j) ### [1, 2, ?]
            print(f"{subset_2=}")

            # if...

            for k in subset_2:
                subset_3 = subset_2 ### [1, 2, ?]
                subset_3.append(k) ### [1, 2, 3]
                print(f"{subset_3=}")

                if len(subset_3) == n:
                    result.update(subset_3)

    return result


def main_single_integers():
    # LIMIT = 100000
    LIMIT = 10**5

    # ### Check if pandigital per int
    # for i in range(LIMIT):
    #     if is_pandigital(i):
    #         print(f"Success with i = {i}")
    #         pass

    # ### Pre-calculate all pandigital numbers
    # pandigital_len_limit = len(str(LIMIT)) - 1 ### E.G For 1000, longest pandigital is 3 digits

    # pandigital_numbers = {1}
    # for i in range(2, pandigital_len_limit + 1):
    #     pandigital_numbers.update(get_all_combinations(i))

    # print(f"{pandigital_numbers=}")

    all_combinations_of_int = get_all_combinations(3)
    print(f"{all_combinations_of_int=}")


def main():
    pass


if __name__ == "__main__":
    # main()
    main_single_integers()
