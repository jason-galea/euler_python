#!/usr/bin/python3

from json import dumps as json_dumps

MAX_LIST_LEN = 15

def main(max_denominator: int):
    result = {
        "denominator": 0,
        "float_s": "",
        "pattern": "",
        "pattern_len": 0
    }

    for denominator in range(2, max_denominator + 1):
        result_f: float = 1 / denominator
        result_decimals_l: list = [
            int(i) for i in
            f"{result_f:.16f}"[2:-1].strip('0')
        ]

        print()
        print(f"1/{denominator} = 0.{join_list(result_decimals_l)}")
        # print(f"result_decimals_l = {result_decimals_l}")
        # print(f"len(result_decimals_l) = {len(result_decimals_l)}")

        discovered_pattern: None | list = find_pattern(result_decimals_l)
        if discovered_pattern:
            print("==> INFO: Found recurring pattern")

            discovered_pattern_len = len(discovered_pattern)
            if discovered_pattern_len > result["pattern_len"]:
                result = {
                    "denominator": denominator,
                    "float_s": f"0.{join_list(result_decimals_l)}",
                    "pattern": join_list(discovered_pattern),
                    "pattern_len": discovered_pattern_len
                }
                print(f"==> INFO: Found new longest pattern! '{result['pattern']}'")


    print()
    print(f"==> INFO: Printing result")
    print(json_dumps(result, indent=4))


def find_pattern(decimals_l: list):

    ### All lists must equal MAX_LIST_LEN
    if len(decimals_l) < MAX_LIST_LEN:
        return


    ### Does any SINGLE int recur
    if decimals_l[-1] == decimals_l[-2]: ### Only check if last two ints match
        for i_pos, i in enumerate(decimals_l):
            pattern = [i]
            list_if_matching = [i] * (MAX_LIST_LEN - i_pos)
            list_subset_to_check = decimals_l[i_pos:]

            # print(f"i_pos = {i_pos}")
            # print(f"i = {i}")
            # print(f"pattern = {pattern}")
            # print(f"list_if_matching = {join_list(list_if_matching)}")
            # print(f"list_subset_to_check = {join_list(list_subset_to_check)}")

            if list_if_matching == list_subset_to_check:
                return pattern

    ### TODO: Does any PATTERN recurr (starting from )

    return


def join_list(l):
    return ''.join([ str(i) for i in l ])


if __name__ == "__main__":
    main(10)
    # main(20)
    # main(100)
    # main(1000)
