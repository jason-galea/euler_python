def main(n1, n2):
    for i in range(n1, n2): # Eg: 6
        # Find fraction
        f = str(1/i)[2:] # Eg: "0.166666666666"
        lenF = len(f)
        longestPattern = ""
        nonRecurringChars = ""
        charBank = f

        # If recurring
        if not (lenF >= 8): continue


        ### 
        for char in f: # Eg: 

            # Check pattern
            patternToCheck = ""
            breakLoop = False
            for char2 in charBank:
                patternToCheck += char2
                lenPossiblePattern = len(patternToCheck)
                possiblePatternLooped = (patternToCheck * (int(lenF / lenPossiblePattern + 1)))[:len(charBank)]

                # print(f"\n{nonRecurringChars} + {possiblePatternLooped} == {nonRecurringChars} + {f[lenPossiblePattern:]}")
                # if ((nonRecurringChars + possiblePatternLooped) == (nonRecurringChars + f[lenPossiblePattern:])):
                # print(f"\n{nonRecurringChars} + {possiblePatternLooped} == {f}")
                if ((nonRecurringChars + possiblePatternLooped) == f):
                    # New recurring pattern found, store
                    print(f"SUCCESS: 0.{f} = 0.{nonRecurringChars}({patternToCheck})")
                    longestPattern = patternToCheck
                    breakLoop = True # The first pattern found is the only valid one, break both loops once found
                    break

                # print(f"{f} = 0.{nonRecurringChars}({patternToCheck})?")
            
            if (breakLoop): break

            ### Move character from START of charBank to END of nonRecurringChars
            # "1" <-- "666"
            # "16" <-- "66"
            nonRecurringChars += charBank[:1]
            charBank = charBank[1:]


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
                lenPossiblePattern = len(possiblePattern)
                possiblePatternLooped = (possiblePattern * (int(lenF / lenPossiblePattern + 1)))[:lenF]

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
                        (lenPossiblePattern > len(longestPattern)) # Wait, doesn't this ALWAYS succeed?
                        and (possiblePattern != (longestPattern * int(len(possiblePattern)/ len(longestPattern))))
                    ):
                        longestPattern = possiblePattern

                    # Handle 1-digit recurring patterns
                    if (lenPossiblePattern == 1):
                        break

            digitsNotRecurring += nonRecChar # TODO: Fix
            pass


            # "166666" --> "6"







        
        # print(f"Longest recurring pattern for 0.{f} was ({longestPattern})")
        print(f"1/{i} = \t0.{f}\n\t0.{digitsNotRecurring}({possiblePattern})")

if __name__ == "__main__":
    # main(6, 7)
    # main(7, 8)
    main(2, 11)
    # main(2, 1001)