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

def is_palindrome(l: list) -> bool:
    """
    [1,2,3,4] --> check up to [1]
    [1,2,3,4,5] --> check up to [1]
    [1,2,3,4,5,6] --> check up to [2]
    """
    length = len(l)
    for i in range(int(length / 2)):
        if not l[i] == l[length - 1 - i]:
            return False
    return True

result = 0

for i in range(1_000_000):
    l = int_to_list_reverse(i)
    b_str = bin(i)[2:]
    b = list(b_str)
    if is_palindrome(l) and is_palindrome(b):
        print(f"Found palindromic int {i} and binary {b_str}")
        result += i

print(f"{result=}")
