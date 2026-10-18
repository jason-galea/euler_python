def is_palindromic_b10():
    pass

def is_palindromic_b2():
    pass

result = 0

for i in range(1_000_000):
    if is_palindromic_b10 and is_palindromic_b2:
        result += i

print(f"{result=}")
