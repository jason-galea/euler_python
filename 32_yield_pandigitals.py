#!/usr/bin/python3


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


def combine_list_of_ints(l: list) -> int:
    result: int = 0
    l.reverse()

    for power_of_ten_to_multiple_i_by, i in enumerate(l):
        result += i * 10**power_of_ten_to_multiple_i_by

    return result


def main():
    digit_limit = 6
    result_products = set()

    for pandigital_l in get_all_combinations_recursive(digit_limit):
    # for pandigital_l in [[1,2,3,4], [4,3,2,1]]:
        # print(f"{pandigital=}")

        ### Search for valid "x * y = z" equations within pandigital number
        valid_split_indices = list( range(1, len(pandigital_l)) ) ### For [1,2,3,4] --> [1,2,3]
        # print(f"{valid_split_indices=}")
        # print(f"{valid_split_indices[:-1]=}")
        # print(f"{valid_split_indices[1:]=}")

        for i in valid_split_indices[:-1]: ### [1,2,3] --> [1,2]
            for j in valid_split_indices[i:]: ### [1,2,3] --> [2,3]
                # print(f"{i=}")
                # print(f"{j=}")

                product = combine_list_of_ints(pandigital_l[j:])

                if product in result_products:
                    continue

                multiplicand = combine_list_of_ints(pandigital_l[:i])
                multiplier = combine_list_of_ints(pandigital_l[i:j])

                if multiplicand * multiplier == product:
                    print(f"{multiplicand} * {multiplier} == {product}")
                    result_products.add(product)



    # check_valid_products([1,2,3,4,5])
    # print(f"{combine_list_of_ints([1,2,3])=}")


if __name__ == "__main__":
    main()
