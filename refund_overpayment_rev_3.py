# Deliverable #3 - Vending Machine Project - Refund
# Description: This program dispenses change (refund) to the user.

# Input: Payment required variable (cost of the ppe) and payment toal (how much the user paid)
# Process: Calculates the overpayment quantity
# Output: Refund quantity

def calculate_refund(payment_total, payment_required):      # Function defined to calculate the refund.
    refund_overpayment = payment_total - payment_required   # Calculate step, using 2 parameters.

    print(f"\nYour refund is: ${refund_overpayment: .2f}\n\n")	    # Display message to the user.

    payment_total = 0   # Resets the cash paid to zero after issuing change.

    return refund_overpayment, payment_total


# if __name__ == '__main__':
#     main()
