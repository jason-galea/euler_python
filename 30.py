#!/usr/bin/python3

def main():
    LIMIT = 1000
    TARGET_POWER = 3

    for i in range(2, LIMIT):

        i_digits = list(str(i))

        total_powers_of_i_digits = 0
        for j in i_digits:
            total_powers_of_i_digits += j**TARGET_POWER

        print(f"{i=}")
        print(f"{total_powers_of_i_digits=}")

        if i == total_powers_of_i_digits:
            print("SUCCESS")


if __name__ == "__main__":
    main()
