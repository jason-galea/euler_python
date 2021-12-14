def main(n1, n2):
    longestPattern = ""
    longestPatternI = ""
    longestPatternString = ""

    for i in range(n1, n2): # Eg: 6
        # Find fraction
        f = str(1/i)[2:] # Eg: "0.166666666666"
        lenF = len(f)
        nonRecurringChars = ""
        charBank = f

        # If recurring
        # if not (lenF >= 8): # This is really stupid, but it works
        #     continue
        # else:
        #     print(f"1/{i} = 0.{f}")


        ### 
        breakLoop = False
        for char in f: # Eg: 

            # Check pattern
            patternToCheck = ""
            for char2 in charBank:
                patternToCheck += char2
                lenPatternToCheck = len(patternToCheck)
                possiblePatternLooped = (patternToCheck * (int(lenF / lenPatternToCheck + 1)))[:len(charBank)]

                # print(f"\n{nonRecurringChars} + {possiblePatternLooped} == {nonRecurringChars} + {f[lenPatternToCheck:]}")
                # if ((nonRecurringChars + possiblePatternLooped) == (nonRecurringChars + f[lenPatternToCheck:])):
                # print(f"\n{nonRecurringChars} + {possiblePatternLooped} == {f}")
                if ((nonRecurringChars + possiblePatternLooped == f)
                    and (lenPatternToCheck != len(possiblePatternLooped)) # Ignore false positives
                ):
                    # New recurring pattern found, store
                    print(f"1/{i} = 0.{nonRecurringChars}({patternToCheck})")
                    if (lenPatternToCheck > len(longestPattern)):
                        longestPattern = patternToCheck
                        longestPatternI = i
                        longestPatternString = f"0.{nonRecurringChars}({patternToCheck})"
                    breakLoop = True # The first pattern found is the only valid one, break both loops once found
                    break

                # print(f"{f} = 0.{nonRecurringChars}({patternToCheck})?")
                
            if (breakLoop): break

            # "1" <-- "666"
            # "16" <-- "66"
            nonRecurringChars += charBank[:1]
            charBank = charBank[1:]

        # If no pattern found
        if  not breakLoop:
            print(f"1/{i} = 0.{f}")

    print(f"\n1/{longestPatternI} had the longest recurring pattern: {longestPatternString}")


def main_better_but_still_broken(n1, n2):
    for i in range(n1, n2):
        # Find fraction
        f = str(1/i)[2:] # 0.33... --> "33..."
        lenF = len(f)
        # digitsNotRecurring = ""
        # possiblePattern = ""
        longestPattern = digitsNotRecurring = ""

        # If recurring
        if not (lenF >= 8): continue


        ### Find recurring pattern
        for nonRecChar in f:
            possiblePattern = ""
            # For every digit in the f
            for ci, char in enumerate(f):
                possiblePattern += char
                lenPatternToCheck = len(possiblePattern)
                possiblePatternLooped = (possiblePattern * (int(lenF / lenPatternToCheck + 1)))[:lenF]

                # "166666" --> char --> Eg. "1"
                # Check if "1" * lenF == f
                if (possiblePatternLooped == f):
                    ### TODO: Reshuffle all this logic
                    # Success?
                    print(f"Found 0.{digitsNotRecurring}({possiblePattern})")
                    
                    # Save longest NON-DUPLICATE pattern. Eg, "123" --> Reject "123123" 
                    if (longestPattern == ""): # Avoids /0 in the elif
                        longestPattern = possiblePattern
                    elif (
                        (lenPatternToCheck > len(longestPattern)) # Wait, doesn't this ALWAYS succeed?
                        and (possiblePattern != (longestPattern * int(len(possiblePattern)/ len(longestPattern))))
                    ):
                        longestPattern = possiblePattern

                    # Handle 1-digit recurring patterns
                    if (lenPatternToCheck == 1):
                        break

            digitsNotRecurring += nonRecChar # TODO: Fix
            pass


            # "166666" --> "6"







        
        # print(f"Longest recurring pattern for 0.{f} was ({longestPattern})")
        print(f"1/{i} = \t0.{f}\n\t0.{digitsNotRecurring}({possiblePattern})")

if __name__ == "__main__":
    # main(6, 7)
    # main(7, 8)
    # main(2, 10)
    main(2, 1000)