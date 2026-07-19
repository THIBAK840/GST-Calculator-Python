import tkinter as tk
from tkinter import ttk, messagebox


def calculate_gst():
    """Calculate GST based on taxable amount, GST rate and transaction type."""

    try:
        taxable_amount = float(amount_entry.get())
        gst_rate = float(gst_rate_var.get())

        if taxable_amount < 0:
            messagebox.showerror(
                "Invalid Amount",
                "Taxable amount cannot be negative."
            )
            return

        total_gst = taxable_amount * gst_rate / 100
        grand_total = taxable_amount + total_gst

        transaction_type = transaction_var.get()

        if transaction_type == "Intra-State (CGST + SGST)":
            cgst = total_gst / 2
            sgst = total_gst / 2

            result_text = (
                f"Taxable Amount : Rs. {taxable_amount:,.2f}\n"
                f"GST Rate       : {gst_rate:.0f}%\n\n"
                f"CGST ({gst_rate / 2:.1f}%)     : Rs. {cgst:,.2f}\n"
                f"SGST ({gst_rate / 2:.1f}%)     : Rs. {sgst:,.2f}\n\n"
                f"Total GST      : Rs. {total_gst:,.2f}\n"
                f"Grand Total    : Rs. {grand_total:,.2f}"
            )

        else:
            result_text = (
                f"Taxable Amount : Rs. {taxable_amount:,.2f}\n"
                f"GST Rate       : {gst_rate:.0f}%\n\n"
                f"IGST ({gst_rate:.0f}%)          : Rs. {total_gst:,.2f}\n\n"
                f"Total GST      : Rs. {total_gst:,.2f}\n"
                f"Grand Total    : Rs. {grand_total:,.2f}"
            )

        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid taxable amount."
        )


def clear_fields():
    """Clear all inputs and reset the calculator."""

    amount_entry.delete(0, tk.END)
    gst_rate_var.set("18")
    transaction_var.set("Intra-State (CGST + SGST)")
    result_label.config(
        text="Enter the details above and click Calculate GST."
    )
    amount_entry.focus()


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()

root.title("GST Calculator - India")
root.geometry("620x650")
root.resizable(False, False)

# ---------------- TITLE ----------------

title_label = tk.Label(
    root,
    text="GST CALCULATOR",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=(25, 5))

subtitle_label = tk.Label(
    root,
    text="CGST • SGST • IGST Calculator",
    font=("Arial", 11)
)

subtitle_label.pack(pady=(0, 20))

# ---------------- INPUT FRAME ----------------

input_frame = ttk.LabelFrame(
    root,
    text="GST Details",
    padding=20
)

input_frame.pack(
    padx=35,
    pady=10,
    fill="x"
)

# Taxable Amount

ttk.Label(
    input_frame,
    text="Taxable Amount (Rs.):"
).grid(
    row=0,
    column=0,
    sticky="w",
    pady=10
)

amount_entry = ttk.Entry(
    input_frame,
    font=("Arial", 12),
    width=25
)

amount_entry.grid(
    row=0,
    column=1,
    padx=15,
    pady=10
)

# GST Rate

ttk.Label(
    input_frame,
    text="GST Rate:"
).grid(
    row=1,
    column=0,
    sticky="w",
    pady=10
)

gst_rate_var = tk.StringVar(value="18")

gst_rate_combo = ttk.Combobox(
    input_frame,
    textvariable=gst_rate_var,
    values=["5", "12", "18", "28"],
    state="readonly",
    width=22
)

gst_rate_combo.grid(
    row=1,
    column=1,
    padx=15,
    pady=10
)

# Transaction Type

ttk.Label(
    input_frame,
    text="Transaction Type:"
).grid(
    row=2,
    column=0,
    sticky="w",
    pady=10
)

transaction_var = tk.StringVar(
    value="Intra-State (CGST + SGST)"
)

transaction_combo = ttk.Combobox(
    input_frame,
    textvariable=transaction_var,
    values=[
        "Intra-State (CGST + SGST)",
        "Inter-State (IGST)"
    ],
    state="readonly",
    width=22
)

transaction_combo.grid(
    row=2,
    column=1,
    padx=15,
    pady=10
)

# ---------------- BUTTONS ----------------

button_frame = tk.Frame(root)

button_frame.pack(pady=15)

calculate_button = ttk.Button(
    button_frame,
    text="Calculate GST",
    command=calculate_gst
)

calculate_button.grid(
    row=0,
    column=0,
    padx=10
)

clear_button = ttk.Button(
    button_frame,
    text="Clear",
    command=clear_fields
)

clear_button.grid(
    row=0,
    column=1,
    padx=10
)

# ---------------- RESULT ----------------

result_frame = ttk.LabelFrame(
    root,
    text="GST Calculation Result",
    padding=20
)

result_frame.pack(
    padx=35,
    pady=10,
    fill="both",
    expand=True
)

result_label = tk.Label(
    result_frame,
    text="Enter the details above and click Calculate GST.",
    font=("Courier New", 11),
    justify="left",
    anchor="nw"
)

result_label.pack(
    fill="both",
    expand=True
)

# ---------------- FOOTER ----------------

footer_label = tk.Label(
    root,
    text="Developed by Thibakkathirravan H | Python Portfolio Project",
    font=("Arial", 9)
)

footer_label.pack(pady=15)

amount_entry.focus()

root.mainloop()
