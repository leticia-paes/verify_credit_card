# This program takes in a credit card number and checks if it is valid, using Luhn algorithm.

"""
https://www.sapling.com/7966257/checksum-credit-card

Verifying a 16-digit card number starts by taking the first 15 digits, which are the institution code and the individual account identifier. For example, in the card number 4578 4230 1376 9219, those digits would be:

4-5-7-8-4-2-3-0-1-3-7-6-9-2-1

Starting with the first digit, multiply every second digit by 2:

8-5-14-8-8-2-6-0-2-3-14-6-18-2-2

Every time you have a two-digit number, just add those digits together for a one-digit result:

8-5-5-8-8-2-6-0-2-3-5-6-9-2-2

Finally, add all the numbers together:

8 + 5 + 5 + 8 + 8 + 2 + 6 + 0 + 2 + 3 + 5 + 6 + 9 + 2 + 2 = 71

When this number is added to the check digit, then the result must be an even multiple of 10. In this case:

71 + 9 = 80

The number is therefore valid. If the algorithm doesn't produce a multiple of 10, then the card number cannot be valid.
"""
from verify_number import verify_credit_card_number

credit_card_number = input('Please inform your credit card number: ')

while credit_card_number.isdigit() == False:
    credit_card_number = input('The information provided is not a number.\nPlease inform your credit card number: ')

while len(credit_card_number) != 16:
    credit_card_number = input('The information provided does not contain 16 digits.\nPlease inform your credit card number: ')

credit_card = []
for digit in map(int,credit_card_number):
    credit_card.append(digit)

verify_credit_card_number(credit_card)





