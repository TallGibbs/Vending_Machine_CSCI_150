# Deliverable #3 - Vending Machine Project
# Description: This program allows PPE to be purchased at a vending machine.
# It will allow for badge, credit card or cash to purchase the items.

# Input: User selects the item to purchase
# Process: Accept payment, then dispense product.
# Output: PPE selected, calculated refund and updated inventory levels.

# Set the main program up so only the function call "main()" is required


# Modularizing the program by using other files to separate primary functions.
import menu_rev_3   # File that contains menu of items to purchase and allows user selection.
import payment_rev_3    # User chooses type of payment and payments validated.
import refund_overpayment_rev_3     # Calculate how much change the user is owed.
import inventory_rev_3      # Update the inventory after item purchased.


def main():
    power_machine_off = 'n'  # Turn machine on and load initial inventory of PPE items.
    items_inventory = [3, 3, 3, 3, 3, 3, 0, 0]  # Initial inventory of PPE.  Used "0" for admin items.
    while power_machine_off != 'y':  # Machine is powered on loop
        purchase_again = 'y'  # Pre-condition state for purchasing loop

        while purchase_again == 'y':  # Purchasing loop

            ppe_selected = menu_rev_3.display_menu()  # See items for sale, make initial selection.

            purchase_again = menu_rev_3.exit_menu(ppe_selected, items_inventory)  # Method to exit menu.

            continue_purchase = "y"     # Initial flag setting so a purchase can occur.

            if ppe_selected > 5:  # Abort purchasing cycle if user selected "view inventory" or "exit menu."
                continue_purchase = 'n'

            while continue_purchase != 'n':  # Continue with the purchase
                payment_required = menu_rev_3.item_cost(ppe_selected)  # Get item's cost from list.

                payment_total = payment_rev_3.main(payment_required)    # Accept & validate payment from the user.

                # Calculate overpayment
                refund_overpayment_rev_3.calculate_refund(payment_total, payment_required)

                inventory_rev_3.update_inventory(ppe_selected, items_inventory)  # Update the inventory after purchase.

                continue_purchase = "n"     # End payment loop so user can return to main menu.

        power_machine_off = input("\nWould you like to shut down the machine to reset inventory levels? "
                                  "Type 'y' to shut down: \n")  # Allows mechanism for inventory to be restocked.

        if power_machine_off == 'y':  # End of loop condition & program will end
            print("\nTurning off vending machine: You can now restock inventory.")


main()  # Calling the main function to run this program

