"""
Find the sum of all numbers which are equal to the sum of the factorial of their digits
NOTE - excluding 1 & 2

Broken down:
- find all numbers equal to the sum of the factorial of their digits
- for each numbe 3 --> inf.
    - break numbers down to their digits
    - for each digit
        - find factorial value
        - add to sum
    - check if sum == number
"""

# from typing import Generator


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
    """145 -> [5,4,1]"""
    ints = []
    while True:
        # print(i)
        if i < 10:
            ints.append(i)
            break

        ints.append(i % 10)
        i = int(i / 10)

    return ints


# def int_to_list_reverse_yeild(i: int) -> Generator[int, None]:
def int_to_list_reverse_yeild(i: int):
    """145 -> [5,4,1]"""
    while True:
        # print(i)
        if i < 10:
            yield i
            break

        yield i % 10
        i = int(i / 10)


def factorial(i: int) -> list:
    if i == 0:
        return 1
    if i < 3:
        return i

    result = 1
    for i in range(2, i + 1):
        result *= i
    return result


### DONE - Pre-compute 0-9 factorial values
### DONE - int_to_list() - Remove slow string concat
### DONE - int_to_list() - yeild
### DONE - ignore 0 in sum loop (SLOWER)
### DONE - exit sum loop if sum > i (SLOWER)
### TODO - pre-compute maximum digit count
def main():
    result = 0

    ### Pre compute factorials
    factorials = [factorial(i) for i in range(10)]
    print(factorials)


    ### Pre compute max digit count
    candidate_digit_length = 1
    while True:
        min_value_for_digit_length = 10**(candidate_digit_length-1)
        max_sum_of_factorials = candidate_digit_length * factorials[9]
        # print(f"{candidate_digit_length=}")
        # print(f"{min_value_for_digit_length=}")
        # print(f"{max_sum_of_factorials=}")
        if min_value_for_digit_length > max_sum_of_factorials:
            break
        candidate_digit_length += 1
    # print(f"Digit length to exceed max possible factorial sum is {candidate_digit_length}")
    upper_bound = (candidate_digit_length - 1) * factorials[9] + 1
    # print(f"Therefor, upper bound is (candidate_digit_length - 1) * factorials[9] + 1 = {upper_bound}")
    # exit()

    # ### DEBUG - track all ints that match length
    # digits_from_length_matched_ints = [0] * 10

    # for i in range(1, 10000):
    # for i in range(3, 999_999):     ### (5650G) NAIVE --> ~3.15 seconds
                                    ### (5650G) PRECOMP --> ~1.6 seconds
                                    ### (9800X3D) PRECOMP --> ~0.51 seconds
                                    ### (9800X3D) INT_LIST_REV --> ~0.29 seconds
                                    ### (9800X3D) YEILD --> ~0.29 seconds
    # for i in range(3, 4_999_999):   ### NAIVE --> ~17.85 seconds
                                    ### PRECOMP --> ~9.15 seconds
                                    ### (9800X3D) YEILD --> ~1.6 seconds
    # for i in range(3, 9_999_999):   ### (9800X3D) YEILD --> ~3.25 seconds
    # for i in range(3, 19_999_999):   ### (9800X3D) YEILD --> ~3.25 seconds
    for i in range(3, upper_bound):
    # for i in [145, 40585]:

        # ints = int_to_list_slow_concat(i)
        ints = int_to_list_reverse(i)
        # print(f"{ints=}")
        sum_of_factorials = 0
        for j in ints:
        # for j in int_to_list_reverse_yeild(i):
            # ### NOTE - SLOWER
            # if j == 0:
            #     continue

            sum_of_factorials += factorials[j]

            # ### NOTE - SLOWER
            # if sum_of_factorials > i:
            #     break

        # print(f"Sum of factorials for digits {i} = {sum_of_factorials}")

        # ### DEBUG
        # if len(ints) == len(str(sum_of_factorials)):
        #     # print(f"{i} has same length of {sum_of_factorials}")
        #     for k in ints:
        #         digits_from_length_matched_ints[k] += 1


        if sum_of_factorials == i:
            print(f"Found int equal to sum of factorials: {i}")
            result += sum_of_factorials

    # ### DEBUG
    # # print(f"{digits_from_length_matched_ints=}")
    # for k, v in enumerate(digits_from_length_matched_ints):
    #     print(f"Int '{k}' found in '{v}' numbers which produced factorial sums of equal length")
    print(f"{result=}")


if __name__ == "__main__":
    main()
