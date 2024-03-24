#!/usr/bin/python3


def get_all_combinations_recursive(
    n=None,
    results=None,
    current_set=None,
    current_combination=None,
):
    """
    For `n`, return list of all combinations of `1..n`
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
    """
    For list of integers, literally combine without addition into single integer.
    E.G: `combine_list_of_ints([1,2,3,4])` returns `1234`
    """
    result: int = 0
    l.reverse()

    for power_of_ten_to_multiply_i_by, i in enumerate(l):
        result += i * 10**power_of_ten_to_multiply_i_by

    return result


def main():
    max_digits = 9
    result_products = set()

    for pandigital_l in get_all_combinations_recursive(max_digits):

        ### Search for valid "x * y = z" equations within pandigital number
        valid_split_indices = pandigital_l.copy()
        valid_split_indices.pop() ### [1,2,3,4] --> [1,2,3]

        for split_1 in valid_split_indices[:-1]: ### [1,2,3] --> [1,2]
            for split_2 in valid_split_indices[split_1:]: ### [1,2,3] --> [2,3]

                product = combine_list_of_ints(pandigital_l[split_2:])

                if product in result_products:
                    continue

                multiplicand = combine_list_of_ints(pandigital_l[:split_1])
                multiplier = combine_list_of_ints(pandigital_l[split_1:split_2])

                if multiplicand * multiplier == product:
                    print(f"{multiplicand} * {multiplier} == {product}")
                    result_products.add(product)

    # print(f"{result_products=}")
    print(f"Sum of products is {sum(result_products)}")


if __name__ == "__main__":
    main()
