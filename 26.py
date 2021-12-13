def main(n1, n2):
    for i in range(n1, n2):
        # Find fraction 
        fraction = str(1/i)[2:] # 0.33... --> "33..."
        longestPattern = ""

        # If recurring
        if not (len(fraction) >= 8): continue

        # Handle 1-digit recurring patterns


        ### Find recurring pattern
        # For every digit in the fraction
        for i, char in enumerate(fraction):
            
            possiblePattern = str(i)
            # Concaternate until length matches fraction
            while (len(possiblePattern) < len(fraction)):
                possiblePattern += str(char)

            # If recurring pattern
            if (possiblePattern[:len(fraction)] == fraction):
                # print(f"Found recurring pattern {possiblePattern} in 0.{fraction}")
                # Save longest pattern
                if (len(possiblePattern) > len(longestPattern)):
                    # print(f"Found new longest p")
                    longestPattern = possiblePattern

        print(f"Longest recurring pattern for 0.{fraction} was ({longestPattern})")


def main_old(n1, n2):
    for i in range(n1, n2):
        # Find fraction 
        fraction = str(1/i)[2:] # 0.33... --> "33..."
        longestPattern = ""

        # If recurring
        if not (len(fraction) >= 8): continue

        ### Find recurring pattern
        # For every digit in the fraction
        for i, char in enumerate(fraction):
            # print(f"{char} ", end="")
            # print(f"Index: {i}\nChar: {char}")
            # print(f"fraction[i:] = {fraction[i:]}")

            # Handle 1-digit recurring patterns
            # THIS BREAKS THE LOOP TOO EARLY
            # if ((char * len(fraction)) == fraction):
            #     print(f"Found recurring pattern ({char}) in 0.{fraction}")
            #     break

            # Loop backwards over all previous chars
            possiblePattern = ""
            
            for j in range(i):
                ### Check if pattern is recurring

                possiblePattern += fraction[j]
                # print(f"Checking if {possiblePattern} == {fraction[j:][:len(possiblePattern)]}")

                if (possiblePattern == fraction[j:][:len(possiblePattern)]):
                    print(f"Found recurring pattern ({possiblePattern}) in 0.{fraction}")

                    if (len(possiblePattern) > len(longestPattern)):
                        longestPattern = possiblePattern
                    break

        print(f"Longest recurring pattern for 0.{fraction} was ({longestPattern})")


if __name__ == "__main__":
    # main(5, 6)
    main(7, 8)
    # main(2, 11)
    # main(2, 1001)