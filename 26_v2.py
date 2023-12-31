#!/usr/bin/python3

from json import dumps as json_dumps

MAX_LIST_LEN: int = 18 ### Max ints to keep when converting float to list

MAX_PATTERN_LEN: int = 14 ### Max pattern length to generate possible matching lists from
### NOTE: Must be < MAX_LIST_LEN
### NOTE: MAX_LIST_LEN/2 is too low, MAX_LIST_LEN - 1 is way too high

def main(max_denominator: int):
    result = {
        "denominator": 0,
        "decimal_f": 0.0,
        "decimal_s": "",
        "pattern_s": "",
        "pattern_len": 0
    }

    for denominator in range(2, max_denominator + 1):
    # for denominator in [9998, 9999]:
        decimal_f: float = 1 / denominator
        decimal_s: str = f"{decimal_f}"[2:][:MAX_LIST_LEN]
        decimal_l: list = list(decimal_s)

        print(f"\n1/{denominator} = {decimal_f}")
        # print(f"==> DEBUG: denominator \t\t= {denominator}")
        print(f"==> DEBUG: decimal_f \t\t= {decimal_f}")
        # print(f"==> DEBUG: decimal_s \t= {decimal_s}")
        print(f"==> DEBUG: decimal_l \t\t= {join_list(decimal_l)}")
        print(f"==> DEBUG: len(decimal_l) \t= {len(decimal_l)}")

        new_pattern: None | list = find_pattern(decimal_l)
        if new_pattern:
            print(f"==> INFO: Found recurring pattern '{join_list(new_pattern)}'")

            new_pattern_len = len(new_pattern)
            if new_pattern_len >= result["pattern_len"]:
                result = {
                    "denominator": denominator,
                    "decimal_f": decimal_f,
                    "decimal_s": decimal_s,
                    "pattern_s": join_list(new_pattern),
                    "pattern_len": new_pattern_len
                }
                print(f"==> INFO: Found new/matching longest pattern len: {new_pattern_len}")
                # print(f"==> DEBUG: {json_dumps(result, indent=4)}")

    print("\n==> INFO: Printing result")
    print(json_dumps(result, indent=4))


def find_pattern(decimals_l: list) -> None | list:

    ### Reject lists obviously unrestricted by float length of ~16-18
    if len(decimals_l) < 10:
        return


    ### Does any SINGLE int recur
    ### NOTE: Only check if last two X match
    repeating_ints_gate: int = 2
    if decimals_l[-repeating_ints_gate:] == decimals_l[-1] * repeating_ints_gate:

        for i_pos, i in enumerate(decimals_l):
            pattern: list = [i]
            list_if_matching: list = [i] * (MAX_LIST_LEN - i_pos)
            list_subset_to_check: list = decimals_l[i_pos:]

            # print(f"i_pos = {i_pos}")
            # print(f"i = {i}")
            # print(f"pattern = {pattern}")
            # print(f"list_if_matching = {join_list(list_if_matching)}")
            # print(f"list_subset_to_check = {join_list(list_subset_to_check)}")

            if list_if_matching == list_subset_to_check:
                return pattern


    ### Does any PATTERN recurr (only starting from [0])
    ### NOTE: Restrict the length of the pattern to reject overly long matches
    for ints_from_start_of_list in range(1, MAX_PATTERN_LEN):
        pattern: list = decimals_l[:ints_from_start_of_list]

        ### Create list of len len(decimals_l), trying to be efficient
        # pattern_len_multiplier = int(MAX_LIST_LEN / len(pattern)) + 1
        # list_if_matching = (pattern * pattern_len_multiplier)[:MAX_LIST_LEN]
        pattern_len_multiplier: int = int(len(decimals_l) / len(pattern)) + 1
        list_if_matching: list = (pattern * pattern_len_multiplier)[:len(decimals_l)]

        # print(f"pattern = {pattern}")
        # print(f"list_if_matching = {join_list(list_if_matching)}")
        # print(f"decimals_l = {join_list(decimals_l)}")

        if list_if_matching == decimals_l:
            return pattern


    ### TODO: Combine above loops into one, checking from [0] --> [-1], THEN iterating
    ### Could loop over range(len(list)), then remove elements from start of list...


def join_list(l: list) -> str:
    return ''.join([ str(i) for i in l ])


if __name__ == "__main__":
    # main(10)
    # main(20)
    # main(50)
    main(100)
    # main(500)
    # main(1000)
    # main(10000)
