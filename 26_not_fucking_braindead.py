#!/usr/bin/python3

MAX_DECIMALS = 12

def main(max_range):

    # for i in range(max_range):
    for i in [7]:
        decimals = generate_decimals(i)

        print()
        print(f"==> DEBUG: decimals = {decimals}")


def generate_decimals(divisor):
    """Perform long division, return decimals"""

    decimals = [0]
    dividend = 10 ### 1, but shifted left
    temp_dividend = dividend

    for _ in range(MAX_DECIMALS):

        dividend_over_divisor = int(temp_dividend / divisor) ### Drop remainder
        decimals.append(dividend_over_divisor)
        result_x_divisor = dividend_over_divisor * divisor

        ### Overwrite var for next loop
        temp_dividend = (temp_dividend - result_x_divisor) * 10

        ### Actually test for previous
        if dividend_over_divisor in decimals[:-1]:
            print(f"==> DEBUG: Found duplicate decimal '{dividend_over_divisor}'")
            # print(f"==> DEBUG: decimals = {decimals}")

            ### Test for multi-char divisors
            ### NOTE: Loop over decimals list backwards, E.G decimals[-1:], decimals[-2:]
            for i in range(len(decimals))

    return decimals


if __name__ == "__main__":
    main(10)
