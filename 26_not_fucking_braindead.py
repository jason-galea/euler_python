#!/usr/bin/python3

def main():
    l = generate_decimals(7)

    print(f"{l=}")


def generate_decimals(divisor):
    """Perform long division, return decimals"""
    decimals = [0]
    max_result = 20

    dividend = 10 ### 1, but shifted left

    for _ in range(max_result):

        dividend_over_divisor = int(dividend / divisor) ### Drop remainder

        decimals.append(dividend_over_divisor)

        result_x_divisor = dividend_over_divisor * divisor


    return decimals


if __name__ == "__main__":
    main()
