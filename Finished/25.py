def fibonacci(): # Yeilds Fibonacci sequence
    f1 = 1
    f2 = 0
    yield f1
    while True:
        temp = f1 + f2
        yield temp
        f2 = f1
        f1 = temp

def main():
    count = 0
    for f in fibonacci():
        count += 1
        # print(f"F({count}) = {f}")
        if (len(str(f)) == 1000):
            print(f"Result = {count}")
            exit(0)

if __name__ == "__main__":
    main()