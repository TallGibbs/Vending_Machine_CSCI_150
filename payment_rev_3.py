# Deliverable #3 - Vending Machine Project - Payment
# Description: This program allows PPE to be paid for.
# It will allow for badge, credit card or cash to be used.

# Input: User selects the method of payment & the badge/credit card number
# Process: Validate type of payment, calculate total payment.
# Output: Payment total


def main(payment_required):
    payment_method = choose_payment_method()  # Payment method variable defined by a function call.

    payment_total = 0   # Initial setting for how much has been paid.

    if payment_method == "1":   # Function call to process employee badge payment.
        payment_total = employee_badge_payment(payment_required)

    if payment_method == "2":   # Function call to process credit card payment.
        payment_total = credit_card_payment(payment_required)

    if payment_method == "3":   # Function call to process cash payment.
        payment_total = cash_payment_option(payment_required)

    return payment_total


def choose_payment_method():    # Menu for user to choose type of payment.
    print("\n")
    print("Please choose your method of payment: \n")
    print("\t1: Employee Badge")
    print("\t2: Credit Card")
    print("\t3: Cash")

    payment_method = input("\nUse the keypad to make a selection: \n")  # Select method of payment.

    while payment_method not in ['1', '2', '3']:  # Input validation loop.
        print("Sorry, that is not a valid selection.  Make another selection\n")
        payment_method = input("\nUse the keypad to make a selection: \n")

    return payment_method


def employee_badge_payment(payment_required):  # Overall function to allow
    # user input of employee badge number & validation.

    employee_badge_id = enter_employee_badge_number()  # Function call to allow user to:
    # enter their employee badge number.

    verify_length(employee_badge_id)  # Function call to verify the badge is 8 characters long.

    payment_total = payment_required    # Charging full product price to their badge number.

    return payment_total


def enter_employee_badge_number():  # Function to allow user to enter their badge number.
    print("\nPlease enter your employee badge number")
    print("Your badge is an 8 digit number: ")

    employee_badge_number = str(input("\n"))  # Allowing any characters as badge number.  Ensure entry is a string
    # so we can get length of it later for validation.

    print(f"\nYou entered:\n\n\t{employee_badge_number}\n\nIs that correct?\n"  # Asking user if correct badge entered.
          f"type 'y' to accept or 'n' to enter again: \n")

    enter_badge_number_correct = input()  # User to accept if entry was correct.

    while enter_badge_number_correct not in ['y', 'n']:  # Validation loop for user to accept or deny entry.
        print("\nSorry, that is not a valid selection.\n"
              "Type 'y' to accept or 'n' to enter again: \n")
        enter_badge_number_correct = input()  # User to accept or deny entry.

    while enter_badge_number_correct == 'n':  # Loop for user to re-enter badge number.
        print("\nPlease enter your employee badge number")
        print("Your badge is an 8 digit number: ")

        employee_badge_number = str(input())  # User enters again to correct their mistake

        print(f"\nYou entered:\n\n\t{employee_badge_number}\n\nIs that correct?\n"
              f"type 'y' to accept or 'n' to enter again: \n")

        enter_badge_number_correct = input()  # User to accept or deny entry.

        while enter_badge_number_correct not in ['y', 'n']:  # Ensure a valid entry is typed.
            print("\nSorry, that is not a valid selection.\n"
                  "Type 'y' to accept or 'n' to enter again: \n")

            enter_badge_number_correct = input()    # Allow user to accept or deny entry.

    return employee_badge_number


def verify_length(employee_badge_number):  # Define the function to verify length of the badge_id entered.
    badge_is_valid = False  # Initial setting for pre-condition test.

    while badge_is_valid is False:  # Loop to verify badge_id entered is valid length of 8 characters.
        characters_in_badge_number = len(employee_badge_number)  # Use length function to
        # count the number of characters.

        if characters_in_badge_number == 8:  # Creating requirement of badge id length.
            badge_is_valid = True
            print("\nThank you.  Your badge number is approved and your account will be charged.")
            print("\nYour payment is made in full.")

        else:
            print("\nSorry, that badge number is not valid.  Must be 8 characters")
            employee_badge_number = enter_employee_badge_number()

    return badge_is_valid


def credit_card_payment(payment_required):  # Overall function to allow user input of credit card number & validation.
    credit_card_number = enter_credit_card_number()  # Function call to allow user to enter their credit card number.

    verify_length_credit_card_number(credit_card_number)  # Function call to verify the credit card is 8 characters long

    payment_total = payment_required    # Charging full product price to their credit card number.

    return payment_total


def enter_credit_card_number():	# Function to allow user to enter their badge number.
    print("\nPlease enter your credit card number")
    print("Your credit card is a 16 digit number: ")

    credit_card_number = str(input("\n"))  # Allowing any characters as credit card number.  Ensure entry is a string
    # so we can get length of it later for validation.

    # Asking user if correct credit card entered.
    print(f"\nYou entered:\n\n\t{credit_card_number}\n\nIs that correct?\n"
          f"type 'y' to accept or 'n' to enter again: \n")

    enter_credit_card_number_correct = input()  # User to accept if entry was correct.

    while enter_credit_card_number_correct not in ['y', 'n']:  # Validation loop for user to accept or deny entry.
        print("\nSorry, that is not a valid selection.\n"
              "Type 'y' to accept or 'n' to enter again: \n")

        enter_credit_card_number_correct = input()  # User to accept or deny entry.

    while enter_credit_card_number_correct == 'n':  # Loop for user to re-enter credit card number.
        print("\nPlease enter your credit card number")
        print("Your credit card is a 16 digit number: ")

        credit_card_number = str(input())  # User enters again to correct their mistake.

        print(f"\nYou entered:\n\n\t{credit_card_number}\n\nIs that correct?\n"
              f"type 'y' to accept or 'n' to enter again: \n")

        enter_credit_card_number_correct = input()  # User to accept or deny entry.

        while enter_credit_card_number_correct not in ['y', 'n']:  # Ensure a valid entry is typed.
            print("\nSorry, that is not a valid selection.\n"
                  "Type 'y' to accept or 'n' to enter again: \n")
            enter_credit_card_number_correct = input()

    return credit_card_number


# Define the function to verify length of the credit card entered.
def verify_length_credit_card_number(credit_card_number):
    credit_card_is_valid = False  # Initial setting for pre-condition test.

    while credit_card_is_valid is False:  # Loop to verify credit card entered is valid length of 16 characters.
        characters_in_credit_card_number = len(credit_card_number)  # Use length function
        # to count the number of characters.

        if characters_in_credit_card_number == 16:  # Creating requirement of credit card length.
            credit_card_is_valid = True

            print("\nThank you.  Your credit card is approved and your account will be charged.")
            print("\nYour payment is made in full.")
        else:
            print("\nSorry, that credit card number is not valid.  The credit card number must be 16 characters")

            credit_card_number = enter_credit_card_number()     # Allow user to re-enter credit card number.

    return credit_card_is_valid


def cash_payment_option(payment_required):	# Function to process cash payment option.
    print("\nPlease deposit your cash: We accept $1, $5, $10 and $20 U.S. bills.")

    payment_total = 0  # Setting accumulation variable.

    deposit_again = "y"  # Pre-test condition for "deposit again" loop.

    # Deposit again loop.
    while deposit_again == "y":  # Checking pre-test condition for "deposit again" loop.
        print("\tPlease choose which U.S. bill you are depositing: \n")
        # print(f"\nReminder: the payment required is ${payment_required: .2f}. \n")
        print("\t1 for $1")
        print("\t5 for $5")
        print("\t10 for $10")
        print("\t20 for $20")

        # Select size of cash payment.
        cash_deposited = str(input("\nUse the keypad to make a selection: \n"))  # Allow any string so program
        # does not crash.  Will convert to float later for summation.

        # Input validation loop.
        while cash_deposited not in ['1', '5', '10', '20']:
            print("Sorry, that is not a valid selection.  Make another selection\n")

            cash_deposited = str(input("\nUse the keypad to make a selection: "))

        cash_deposited = float(cash_deposited)  # Converting to a float to allow summation.

        payment_total = payment_total + cash_deposited  # Accumulation variable being updated.

        print("\n__________________________________")
        print("***DEPOSIT TOTAL***")
        print(f"\nTotal cash deposited is ${payment_total:.2f}")
        print("__________________________________\n")

        # Checking to see if any more cash to deposit.
        deposit_again = input("Do you have anymore cash to deposit? \n"
                              "Type 'y' to deposit again or 'n' to finish.\n")

        remaining_payment = payment_required - payment_total    # Calculate how much more cash is required.

        if remaining_payment > 0:   # Give user warning they need to pay more cash.
            deposit_again = 'y'
            print(f"\nThe remaining balance to be paid is: ${remaining_payment: .2f}")
            print("\nYou must deposit more money so the transaction can be completed.")

        # Input validation loop.
        while deposit_again not in ["y", "n"]:
            print("Sorry, that is not a valid selection.  Make another selection\n")
            deposit_again = input("Do you have anymore cash to deposit? \n\n"
                                  "Type 'y' to deposit again or 'n' to finish.")

    return payment_total


if __name__ == '__main__':
    main()

