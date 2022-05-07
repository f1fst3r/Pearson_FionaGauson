
def main():
    while True:
        ex_choice = disp_main_menu()
        if (ex_choice == 'Q'):
            break

        disp_ex_handler(ex_choice)

# -------------------------------------------------------------------------------
# region Display Helpers


def disp_main_menu():
    '''
    Display method: Displays the main menu to allow the user to choose an
    exercise to test.
    '''

    print("-----------------------------------------------")
    print("--------------- << MAIN MENU >> ---------------")
    print("Select exercise:")
    print("\t 1 : Palindromes")
    print("\t 2 : Romans")
    print("\t 3 : Fibonacci")
    print("\t 4 : Coin change")
    print("Or type 'Q' to quit.")

    while True:
        choice = input()
        if (choice == 'Q'):
            return choice
        try:
            choice = int(choice)
        except ValueError:
            choice = 0

        if (choice >= 1 and choice <= 4):
            break
        else:
            print("!! Please enter a valid selection")

    print("----------------------------------------------")
    return choice


def disp_ex_handler(ex_choice):
    '''
    Display method: Handles selection of execises, testing, and user input.
    '''

    if (ex_choice == 1):
        print("---------------- Palindromes -----------------")

        if (disp_test_handler()):
            test, expected = ex1_test()
            for i in range(0, len(test) - 1):
                # test and expected will be of equal length
                result = ex1_palindrome(test[i])
                disp_test_compare(test[i], result, expected[i])
            print("Press enter to continue...")
            input()

        else:
            while True:
                print("Enter string: (Or just press enter to quit)")
                user_input = input()
                if (user_input == ""):
                    break
                result = ex1_palindrome(user_input)
                print(f"Result: {result}")

    elif (ex_choice == 2):
        print("------------------- Romans -------------------")

        if (disp_test_handler()):
            test, expected = ex2_test()
            for i in range(0, len(test) - 1):
                # test and expected will be of equal length
                result = ex2_romans(test[i])
                disp_test_compare(test[i], result, expected[i])
            print("Press enter to continue...")
            input()

        else:
            while True:
                print("Enter positive integer: (Or just press enter to quit)")
                user_input = input()

                # Validation of user input
                if (user_input == ""):
                    break
                try:
                    user_input = int(user_input)
                except ValueError:
                    print("!! Please enter a valid integer")
                    continue
                if (user_input < 0):
                    print("!! Please enter a valid integer")
                    continue

                result = ex2_romans(user_input)
                print(f"Result: {result}")

    elif (ex_choice == 3):
        print("----------------- Fibonacci ------------------")

        if (disp_test_handler()):
            print("No test cases available for this exercise.")
            print("Press enter to continue...")
            input()

        else:
            while True:
                print("Enter positive integer: (Or just press enter to quit)")
                user_input = input()

                # Validation of user input
                if (user_input == ""):
                    break
                try:
                    user_input = int(user_input)
                except ValueError:
                    print("!! Please enter a valid integer")
                    continue
                if (user_input < 0):
                    print("!! Please enter a valid integer")
                    continue

                result, fib_nums = ex3_fibonacci(user_input)
                print(f"Result: {result}")

                seq = ''
                # Show user number breakdown
                for num in fib_nums:
                    seq += f'{num}, '

                seq = seq.rstrip(', ')
                print("\tSequence Summed:")
                print(f"\t ({seq})")

    else:  # ex_choice can only have 4 at this point
        print("---------------- Coin Change -----------------")
        if (disp_test_handler()):
            test, expected = ex4_test()
            for i in range(0, len(test) - 1):
                # test and expected will be of equal length
                result, _ = ex4_coin_change(test[i])
                disp_test_compare(test[i], result, expected[i])
            print("Press enter to continue...")
            input()
        else:
            while True:
                print("Enter positive integer: (Or just press enter to quit)")
                user_input = input()

                # Validation of user input
                if (user_input == ""):
                    break
                try:
                    user_input = int(user_input)
                except ValueError:
                    print("!! Please enter a valid integer")
                    continue
                if (user_input < 0):
                    print("!! Please enter a valid integer")
                    continue

                result, coins = ex4_coin_change(user_input)
                print(f"Result: {result} coins")

                # Show user coin breakdown
                print("\tCoins:")
                for i in range(0, len(coins[0])):
                    num_coins = coins[0][i]
                    val_coins = coins[1][i]

                    if (num_coins == 0):
                        continue
                    print(f"\t  {num_coins} x {val_coins}p")


def disp_test_handler():
    '''
    Display method: Displays prompts for user to choose whether to run test
    cases.
    '''

    print("Would you like to use test cases? (y/n)")
    while True:
        choice = input()
        if (choice == 'y' or choice == 'n'):
            break
        else:
            print("!! Please enter a valid selection")

    if (choice == 'n'):
        return False
    else:
        return True


def disp_test_compare(input, result, expected):
    '''
    Display Method: Displays test results
    '''
    valid = (result == expected)
    print(f"For input '{input}': \t{valid}")
    print(f"\t Result:   {result}")
    print(f"\t Expected: {expected}")


# endregion Display Helpers

# -------------------------------------------------------------------------------
# region Exercise 1
def ex1_palindrome(test_string):
    '''
    Exercise 1: Palindrome 

    Takes an input of a string and returns True if the string is a palindrome,
    False if the string is not a palindrome.
    '''

    # Split string by character
    char_arr = list(test_string)

    # Split array into halves (centre character is irrelevant if odd)
    # Hence cast to an int since that's the equivalent of floor
    lenArr = len(char_arr)  # storing this to improve performance
    halfLen = int(lenArr/2)
    arr_1 = char_arr[: halfLen]

    tes = (lenArr - halfLen)
    arr_2 = char_arr[tes:]

    # reverse arr_2 and check for equivalence between array values
    arr_2.reverse()

    isPalindrome = True
    for i in range(0, halfLen):
        if not (arr_1[i] == arr_2[i]):
            isPalindrome = False
            break

    return isPalindrome


def ex1_test():
    '''
    Test Method: Holds test and expected values for Exercise 1: Palindromes
    '''

    test = ['hello', 'kayak', 'parrot', 'tomorrow', 'racecar', 'noon']
    expected = [False, True, False, False, True, True]
    return test, expected

# endregion Exercise 1

# -------------------------------------------------------------------------------
# region Exercise 2


def ex2_romans(plain_int):
    '''
    Exercise 2: Romans

    Takes an input of an integer and returns the equivalent in Roman numerals.

    '''

    ordered_table = [
        [1, 'I'],
        [4, 'IV'],  # see below comment for why I've added this entry
        [5, 'V'],
        [9, 'IX'],  # see below
        [10, 'X'],
        [40, 'XL'],  # see below
        [50, 'L'],
        [90, 'XC'],  # see below
        [100, 'C'],
        [400, 'CD'],  # see below
        [500, 'D'],
        [900, 'CM'],  # see below
        [1000, 'M']
    ]
    # intial array is arranged so it's more human readable
    ordered_table.reverse()

    '''
    NB: We can only 'subtract' powers of 10 from the two letters 'above' it 
    ie: I can only be 'subtracted' from V and X; X from L and C etc.
    eg: 49 => XLIX =/= IL

    This added complexity means that I've decided to enter 4, 9 etc. into the
    above ordered table for performance, checking for the above condition is 
    far more complex than adding entries.
    '''

    roman_int = ''

    for conv_pair in (ordered_table):
        unit_val = conv_pair[0]
        letter_val = conv_pair[1]

        while (plain_int >= unit_val):
            plain_int -= unit_val
            roman_int += letter_val

    return roman_int


def ex2_test():
    '''
    Test Method: Holds test and expected values for Exercise 2: Romans
    '''

    test = [39, 246, 789, 2421, 18, 2022, 49, 949]
    expected = ['XXXIX', 'CCXLVI', 'DCCLXXXIX', 'MMCDXXI', 'XVIII',
                'MMXXII', 'XLIX', 'CMXLIX']
    return test, expected

# endregion Exercise 2

# -------------------------------------------------------------------------------
# region Exercise 3


def ex3_fibonacci(user_input):
    '''
    Exercise 3: Fibonacci

    Takes an integer input and returns for said n: the sum of the Fibonacci
    numbers up to, but not including n. 

    NB: I found this exercise unclear and would be keen to discuss if this 
    solution was not what was required.
    '''

    if user_input < 1:
        return 0

    # Let's take c = a + b where a <= b
    a = 0  # f0
    b = 1  # f1
    c = a + b

    fib_sums = [a, b, c]  # stores all the fibonacci numbers to sum

    while (c < user_input):
        a = b
        b = c
        c = a + b
        fib_sums.append(c)

    # remove the last value as this will be > n
    fib_sums = fib_sums[0: -1]

    return sum(fib_sums), fib_sums

# endregion Exercise 3

# -------------------------------------------------------------------------------
# region Exercise 4


def ex4_coin_change(change_rem):
    '''
    Exercise 4: Coin Change

    Takes an integer input and returns the minimum number of coins required to
    reach said total, also returns a multidimensional array of 
    [coin_count, coin_vals] to show the user what coins were required.
    '''

    coin_values = [1, 2, 5, 10, 20, 50, 100]
    # initial array is arranged so it's more human readable
    coin_values.reverse()

    coin_count = []

    for coin in (coin_values):
        count = 0
        while (change_rem >= coin):
            change_rem -= coin
            count += 1
        coin_count.append(count)

    result_arr = [coin_count, coin_values]

    return sum(coin_count), result_arr


def ex4_test():
    '''
    Test Method: Holds test and expected values for Exercise 4: Coin Change
    '''

    test = [39, 107, 65, 83]
    expected = [6, 3, 3, 5]
    return test, expected

# endregion Exercise 4

# -------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
