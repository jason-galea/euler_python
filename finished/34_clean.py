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


result = 0

### Pre compute factorials
factorials = [factorial(i) for i in range(10)]
print(factorials)

### Pre compute max digit count
candidate_digit_length = 1
while True:
    min_value_for_digit_length = 10**(candidate_digit_length-1)
    max_sum_of_factorials = candidate_digit_length * factorials[9]
    if min_value_for_digit_length > max_sum_of_factorials:
        break
    candidate_digit_length += 1
upper_bound = (candidate_digit_length - 1) * factorials[9] + 1

for i in range(3, upper_bound):
    sum_of_factorials = 0
    for j in int_to_list_reverse_yeild(i):
        sum_of_factorials += factorials[j]

    if sum_of_factorials == i:
        result += sum_of_factorials

print(f"{result=}")
