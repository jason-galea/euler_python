#!/usr/bin/python3


def digitize(n, base=10):
    """
    Convert integer 'n' into a list of it's digits.
    E.G: list(digitize(1234)) --> [1, 2, 3, 4]
    """
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
    print(f"Entered 'get_all_combinations()'")
    print(f"{n=}")

    combinations = []
    complete_set = list(range(1, n + 1)) ### [1, 2, 3]

    for i_pos, i in enumerate(complete_set): ### 1 --> 2 --> 3
        subset_1 = [i] ### [i, ?, ?]

        # print(f"{subset_1=}")

        # if...

        next_subset_1 = complete_set.copy()
        next_subset_1.pop(i_pos)
        # print(f"{next_subset_1=}")

        for j_pos, j in enumerate(next_subset_1): ### 2 --> 3
            subset_2 = subset_1 + [j] ### [i, j, ?]

            # print(f"{subset_2=}")

            # if...

            next_subset_2 = next_subset_1.copy()
            next_subset_2.pop(j_pos)
            # print(f"{next_subset_2=}")

            for k_pos, k in enumerate(next_subset_2): ### 2 --> 3
                subset_3 = subset_2 + [k] ### [i, j, k]
                # print(f"{subset_3=}")


                if len(next_subset_2) == 1:
                    combinations.append(subset_3)
                    continue

                # _next_subset_3 = next_subset_2.copy()
                # _next_subset_3.pop(k_pos)
                # print(f"{_next_subset_3=}")

    return combinations


def get_all_combinations_recursive(
    n=None,
    results=None,
    current_set=None,
    current_combination=None,
):
    """
    For 'n', return list of all combinations of 1..n
    """

    # print(f"Entered 'get_all_combinations_recursive()'")
    # print(f"{n=}")
    # print(f"{results=}")
    # print(f"{current_set=}")
    # print(f"{current_combination=}")

    if n and not current_set: ### First iteration
        results = []
        current_set = list(range(1, n + 1))
        # current_combination = [current_set[0]]
        current_combination = []

    for i_pos, i in enumerate(current_set):
        next_combination = current_combination + [i]

        if len(current_set) == 1: ### Last iteration, exit & return
            results.append(next_combination)
            continue

        ### Else, next iteration
        next_set = current_set.copy()
        next_set.pop(i_pos)
        results = get_all_combinations_recursive(
            results=results,
            current_set=next_set,
            current_combination=next_combination
        )

    return results


def main_single_integers():
    # LIMIT = 100000
    LIMIT = 10**5

    ### Check if pandigital per int
    pandigital_numbers = []
    for i in range(LIMIT):
        if is_pandigital(i):
            print(f"Success with i = {i}")
            pandigital_numbers.append(i)

    # ### Pre-calculate all pandigital numbers
    # pandigital_len_limit = len(str(LIMIT)) - 1 ### E.G For 1000, longest pandigital is 3 digits

    # pandigital_numbers = {1}
    # for i in range(2, pandigital_len_limit + 1):
    #     pandigital_numbers.update(get_all_combinations(i))


    # all_combinations_of_int = get_all_combinations_recursive(2)
    # print(f"{all_combinations_of_int=}")
    # # all_combinations_of_int = get_all_combinations(3)
    # all_combinations_of_int = get_all_combinations_recursive(3)
    # print(f"{all_combinations_of_int=}")
    # all_combinations_of_int = get_all_combinations_recursive(4)
    # print(f"{all_combinations_of_int=}")

    print(f"{pandigital_numbers=}")
    # print(f"Sum of all pandigital numbers is: {sum(pandigital_numbers)}")


def main():
    pandigital_products = set()
    exit_loop = False
    # product = 1
    product = 3096 ### First pandigital product

    while not exit_loop:
        for multiplier in range(2, int(product**0.5) + 1):

            multiplicand, remainder = divmod(product, multiplier)

            if remainder == 0:
                # print(f"{multiplicand} x {multiplier} = {product}")

                all_digits = (
                    list(digitize(multiplicand))
                    + list(digitize(multiplier))
                    + list(digitize(product))
                )

                # if len(all_digits) >= 10:
                #     exit_loop = True

                # if len(all_digits) == len(set(all_digits)) == 9:
                if len(all_digits) == len(set(all_digits)):
                    print(f"{len(set(all_digits))}")
                    print(f"{multiplicand} x {multiplier} = {product}")
                    pandigital_products.add(product)

        product += 1

    print(f"{pandigital_products=}")
    print(f"Sum of pandigital products is {sum(pandigital_products)}")



if __name__ == "__main__":
    main()
    # main_single_integers()
