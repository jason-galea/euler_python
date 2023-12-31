#!/usr/bin/python3

def main():
    l = generate_decimals(7)

    print(f"{l=}")


def generate_decimals(divisor):
    """Perform long division, return decimals"""
    decimals = [0]
    max_result = 10

    dividend = 10 ### 1, but shifted left

    temp_dividend = dividend

    for _ in range(max_result):

        dividend_over_divisor = int(temp_dividend / divisor) ### Drop remainder
        decimals.append(dividend_over_divisor)

        result_x_divisor = dividend_over_divisor * divisor

        ### Overwrite var for next loop
        temp_dividend = (temp_dividend - result_x_divisor) * 10

        print()
        print(f"==> DEBUG: dividend = {dividend}")
        print(f"==> DEBUG: dividend_over_divisor = {dividend_over_divisor}")
        print(f"==> DEBUG: result_x_divisor = {result_x_divisor}")
        print(f"==> DEBUG: temp_dividend = {temp_dividend}")

    # next_dividend_over_divisor = int( dividend_minus_result / divisor )
    # decimals.append(next_dividend_over_divisor)

    # next_result_x_divisor = next_dividend_over_divisor * divisor

    # print(f"==> DEBUG: next_dividend_over_divisor = {next_dividend_over_divisor}")
    # print(f"==> DEBUG: next_result_x_divisor = {next_result_x_divisor}")



    return decimals


if __name__ == "__main__":
    main()
