#!/usr/bin/python3

from json import dumps as json_dumps

MAX_LIST_LEN: int = 18 ### Max ints to keep when converting float to list

MAX_PATTERN_LEN: int = 15 ### Max pattern length to generate possible matching lists from
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

    # for denominator in range(2, max_denominator + 1):
    for denominator in [14]:
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

    ### Combine above loops into one, checking from [0] --> [-1], THEN iterating
    for i in range(len(decimals_l)):
        decimals_l_subset = decimals_l[i:]
        print()
        print(f"==> DEBUG: {join_list(decimals_l_subset)=}")

        for ints_from_start_of_list in range(1, MAX_PATTERN_LEN):
            pattern: list = decimals_l_subset[:ints_from_start_of_list]

            ### Create list of len len(decimals_l_subset), trying to be efficient
            # pattern_len_multiplier = int(MAX_LIST_LEN / len(pattern)) + 1
            # list_if_matching = (pattern * pattern_len_multiplier)[:MAX_LIST_LEN]
            pattern_len_multiplier: int = int(len(decimals_l_subset) / len(pattern)) + 1
            list_if_matching: list = (pattern * pattern_len_multiplier)[:len(decimals_l_subset)]

            print(f"pattern = {pattern}")
            print(f"list_if_matching = {join_list(list_if_matching)}")
            print(f"decimals_l_subset = {join_list(decimals_l_subset)}")

            if list_if_matching == decimals_l_subset:
                return pattern



def join_list(l: list) -> str:
    return ''.join([ str(i) for i in l ])


if __name__ == "__main__":
    # main(10)
    main(20)
    # main(50)
    # main(100)
    # main(500)
    # main(1000)
    # main(10000)
