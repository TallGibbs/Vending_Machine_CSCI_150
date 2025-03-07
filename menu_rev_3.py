# Chris Gibbs
# Deliverable #3 - Vending Machine Project - Menu Function
# Description: This function displays PPE for sale and allows selection for purchase.
# It will also display the cost of the item chosen by the user.

# Input: User selects the item to purchase
# Process: Validates input is acceptable.  Adjusts the "ppe_selected" variable so the selection number
# matches the index position of the ppe in the list.
# Output: PPE selected cost and method to exit menu, if chosen.


def display_menu():     # Initial function that user will see to make selection
    items_to_vend = ["Safety Glasses", "Ear Plugs", "Welding Gloves", "Nitrile Gloves", "Nomex Hood", "Flint Striker",
                     "View Inventory", "Exit Purchase"]
    print("\n")
    print("Welcome to our PPE vending machine: what would you like to purchase? \n")
    print("Here are the items we sell:")
    print("\t1: Safety Glasses")	# Future work: display this as the element of the list vs. hard coding it.
    # All lines below
    print("\t2: Ear Plugs")
    print("\t3: Welding Gloves")
    print("\t4: Nitrile Gloves")
    print("\t5: Nomex Hood")
    print("\t6: Flint Striker")
    print("\n\t----ADMIN----")
    print("\t7: View Inventory")
    print("\t8: Exit Purchase")

    ppe_selected = input("\nUse the keypad to make a selection: \n")   # Item chosen to purchase.

    while ppe_selected not in ['1', '2', '3', '4', '5', '6', '7', '8']:  # Input validation loop.
        print("Sorry, that is not a valid selection.  Make another selection\n")
        ppe_selected = input("\nUse the keypad to make a selection: ")   # Enter selection again.

    ppe_selected = int(ppe_selected) - 1    # Convert to an integer & match the index position from the list

    print(f"\nYou chose: {items_to_vend[ppe_selected]}. ")  # Let user see what they chose.

    input("\nHit any key to continue: ")    # Pause break so user can move on when ready.

    return ppe_selected


def exit_menu(ppe_selected, items_inventory):    # Allows method to return to menu
    if ppe_selected == 7:     # PPE selected was reduced by 1 in previous function to have list indices & input match
        purchase_again = 'n'  # Let user exit the purchasing loop

    elif ppe_selected == 6:
        print("\nHere is inventory of all items: \n")  # Sequence of lines to show updated inventory
        print(f"Safety Glasses: \t{items_inventory[0]}")
        print(f"Ear Plugs: \t\t\t{items_inventory[1]}")
        print(f"Welding Gloves: \t{items_inventory[2]}")
        print(f"Nitrile Gloves: \t{items_inventory[3]}")
        print(f"Nomex Hood: \t\t{items_inventory[4]}")
        print(f"Flint Striker: \t\t{items_inventory[5]}")
        input("\nTake a second to view the inventory.  Hit any key to return to main menu: ")
        purchase_again = 'y'

    else:
        purchase_again = 'y'    # Standard will be 'y' so purchasing can continue.

    return purchase_again


def item_cost(ppe_selected):    # Defining the cost of each item.  Chose $0 for the ADMIN item selections.
    ppe_cost = [13, 1.25, 25, 0.72, 11.86, 23, 0, 0]
    payment_required = ppe_cost[ppe_selected]   # Grabbing the cost from the list.
    print(f"\nThe payment required is ${payment_required: .2f}. ")  # Show the item's cost to the user.
    return payment_required

# Chose not to make this a main and to just call each function individually.

