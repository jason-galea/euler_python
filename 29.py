def count_of_distinct_terms(a_limit, b_limit):
    distinct_terms = set()

    for a in range(2, a_limit + 1):
        for b in range(2, b_limit + 1):
            print(f"a = {a}, b = {b}")

if __name__ == "__main__":
    count_of_distinct_terms(5, 5)
    # count_of_distinct_terms(100, 100)