# GST Calculator - Python
# Created by Thibakkathirravan H

print("=" * 45)
print("           GST CALCULATOR - INDIA")
print("=" * 45)

try:
    taxable_amount = float(input("Enter taxable amount (Rs.): "))

    print("\nAvailable GST Rates:")
    print("1. 5%")
    print("2. 12%")
    print("3. 18%")
    print("4. 28%")

    gst_rate = float(input("\nEnter GST rate (5, 12, 18, or 28): "))

    if gst_rate not in [5, 12, 18, 28]:
        print("\nInvalid GST rate. Please choose 5, 12, 18, or 28.")

    elif taxable_amount < 0:
        print("\nTaxable amount cannot be negative.")

    else:
        print("\nTransaction Type:")
        print("1. Intra-State (CGST + SGST)")
        print("2. Inter-State (IGST)")

        transaction_type = input("\nEnter 1 or 2: ")

        total_gst = taxable_amount * gst_rate / 100
        grand_total = taxable_amount + total_gst

        print("\n" + "=" * 45)
        print("              GST CALCULATION")
        print("=" * 45)

        print(f"Taxable Amount : Rs. {taxable_amount:,.2f}")
        print(f"GST Rate       : {gst_rate:.0f}%")

        if transaction_type == "1":

            cgst = total_gst / 2
            sgst = total_gst / 2

            print("\nTransaction    : Intra-State")
            print(f"CGST ({gst_rate / 2:.1f}%)    : Rs. {cgst:,.2f}")
            print(f"SGST ({gst_rate / 2:.1f}%)    : Rs. {sgst:,.2f}")

        elif transaction_type == "2":

            print("\nTransaction    : Inter-State")
            print(f"IGST ({gst_rate:.0f}%)       : Rs. {total_gst:,.2f}")

        else:
            print("\nInvalid transaction type.")
            exit()

        print("-" * 45)
        print(f"Total GST      : Rs. {total_gst:,.2f}")
        print(f"Grand Total    : Rs. {grand_total:,.2f}")
        print("=" * 45)

except ValueError:
    print("\nInvalid input. Please enter numbers only.")
