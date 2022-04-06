#defining the function that will verify the credit card number

def verify_credit_card_number(credit_card_number):
    #take the first 15 digits, separate from last digit:
    first_15_digits = []
    for i in range(15):
        first_15_digits.append(credit_card_number[i])

    last_digit = credit_card_number[-1]

    #Starting with the first digit, multiply every second digit by 2:
    mult_numbers = []
    i = 0
    while i < 15:
        mult_numbers.append(first_15_digits[i]*2)
        i = i + 2

    #Every time you have a two-digit number, just add those digits together for a one-digit result:

    for num in mult_numbers:
        if num > 9:
            r = 0
            i = mult_numbers.index(num)
            for digit in str(mult_numbers[i]):
                r += int(digit)

            mult_numbers[i] = r

    #Get the numbers that were not multiplied by two and add them:

    outside_digits = []
    a = 1
    while a < 15:
        outside_digits.append(first_15_digits[a])
        a = a + 2

    outside_digits_sum = 0
    for digit in outside_digits:
        outside_digits_sum += digit

    #Finally, add all the numbers together:
    digits_sum = 0
    for digit in mult_numbers:
        digits_sum += digit

    #When this number is added to the check digit(the last digit of the credit card), then the result must be an even multiple of 10. In this case:
    total_sum = digits_sum + last_digit + outside_digits_sum
    if total_sum % 10 == 0 and total_sum % 2 == 0:
        print('The credit card number is valid.')
    else:
        print('The credit card number is not valid.')