def main():
    # for i in range(2, 1001):
    for i in range(2, 10):
        # Find fraction 
        fraction = 1/i

        # If recurring
        if not (len(str(fraction)) >= 10): continue

        # Find recurring pattern

        print (fraction)

if __name__ == "__main__":
    main()