def factorial(i: int) -> int:
    if i < 3:
        return i

    result = 1
    for i in range(2, i + 1):
        result *= i
    return result

for i in range(10):
# for i in [4]:
    print(f"factorial({i}) = {factorial(i)}")