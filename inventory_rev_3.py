# Chris Gibbs
# Deliverable #3 - Vending Machine Project - Inventory
# Description: This program updates the inventory levels after PPE is purchased

# Input: PPE selected & inventory list of PPE
# Process: Determine which PPE inventory to update, also allow user to view inventory.
# Output: Updated inventory list variable and display inventory if user chooses.


# Reminder: Here is the list of what we are vending:
# items_to_vend = ["Safety Glasses", "Ear Plugs", "Welding Gloves", "Nitrile Gloves", "Nomex Hood", "Flint Striker",
#                      "View Inventory", "Close Program"]

def update_inventory(ppe_selected, items_inventory):    # Function to update inventory using 2 parameters.
    index_position = ppe_selected  # Identify the index position in the list when ppe is selected.

    if index_position != 6 or 7:    # If "ADMIN" options chosen, do not update inventory of those items.
        items_inventory[index_position] = items_inventory[index_position] - 1   # Reduce the current inventory by 1
    # Want to make this only happen when "non-admin" items are chosen.  Improvement feature.
        if items_inventory[index_position] == 1 or 0:
            print("**ATTENTION**")
            print(f"There is only {items_inventory[index_position]} more of this item in stock.  "
                  f"Please alert supervisor.\n")

            input("Hit any key to continue.\n")

        if items_inventory[index_position] < 0:
            print("*********** OUT OF STOCK ***********")
            print("This item is not in stock.  Please take a picture of this message.\n"
                  "You will need this to request a refund.\n")

            input("Please take your photo, then hit any key to continue.\n")

    view_updated_inventory = input("Would you like to view the updated inventory?\n"
                                   "\tType 'y' to view the inventory or \n"
                                   "\tType 'n' to skip: ")

    while view_updated_inventory not in ['y', 'n']:  # Validation loop for user to accept or deny entry
        print("\nSorry, that is not a valid selection.\n"
              "Type 'y' to view the inventory or 'n' to skip: \n")
        view_updated_inventory = input()  # User to accept or deny entry

    if view_updated_inventory == 'y':	    # Actual display of updated inventory.

        print("\nHere is the updated inventory of all items: \n")  # Sequence of lines to show updated inventory
        print(f"Safety Glasses: \t{items_inventory[0]}")
        print(f"Ear Plugs: \t\t\t{items_inventory[1]}")
        print(f"Welding Gloves: \t{items_inventory[2]}")
        print(f"Nitrile Gloves: \t{items_inventory[3]}")
        print(f"Nomex Hood: \t\t{items_inventory[4]}")
        print(f"Flint Striker: \t\t{items_inventory[5]}")
        input("\nTake a second to view the inventory.  Hit any key to return to main menu: ")

        # Future work: add method for sending "low inventory" signal.
        # Open a file and have this logged (append mode), ideally with time stamp for reference.

    return items_inventory


# if __name__ == '__main__':
#     main()

