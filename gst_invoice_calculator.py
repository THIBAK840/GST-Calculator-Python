import tkinter as tk
from tkinter import ttk, messagebox


class GSTInvoiceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("GST Invoice Calculator - India")
        self.root.geometry("1050x700")

        self.items = []

        self.create_header()
        self.create_input_section()
        self.create_table()
        self.create_summary()

    def create_header(self):
        title = tk.Label(
            self.root,
            text="GST INVOICE CALCULATOR",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=(20, 5))

        subtitle = tk.Label(
            self.root,
            text="Multiple Items • CGST • SGST • IGST • Invoice Summary",
            font=("Arial", 11)
        )
        subtitle.pack(pady=(0, 15))

    def create_input_section(self):
        frame = ttk.LabelFrame(
            self.root,
            text="Add Invoice Item",
            padding=15
        )
        frame.pack(fill="x", padx=25, pady=10)

        ttk.Label(frame, text="Description").grid(
            row=0, column=0, padx=5, pady=5
        )

        self.description_entry = ttk.Entry(frame, width=22)
        self.description_entry.grid(
            row=1, column=0, padx=5, pady=5
        )

        ttk.Label(frame, text="Quantity").grid(
            row=0, column=1, padx=5, pady=5
        )

        self.quantity_entry = ttk.Entry(frame, width=12)
        self.quantity_entry.grid(
            row=1, column=1, padx=5, pady=5
        )

        ttk.Label(frame, text="Rate (Rs.)").grid(
            row=0, column=2, padx=5, pady=5
        )

        self.rate_entry = ttk.Entry(frame, width=15)
        self.rate_entry.grid(
            row=1, column=2, padx=5, pady=5
        )

        ttk.Label(frame, text="GST Rate").grid(
            row=0, column=3, padx=5, pady=5
        )

        self.gst_var = tk.StringVar(value="18")

        self.gst_combo = ttk.Combobox(
            frame,
            textvariable=self.gst_var,
            values=["5", "12", "18", "28"],
            state="readonly",
            width=10
        )
        self.gst_combo.grid(
            row=1, column=3, padx=5, pady=5
        )

        ttk.Label(frame, text="Transaction Type").grid(
            row=0, column=4, padx=5, pady=5
        )

        self.transaction_var = tk.StringVar(
            value="Intra-State"
        )

        self.transaction_combo = ttk.Combobox(
            frame,
            textvariable=self.transaction_var,
            values=[
                "Intra-State",
                "Inter-State"
            ],
            state="readonly",
            width=15
        )
        self.transaction_combo.grid(
            row=1, column=4, padx=5, pady=5
        )

        ttk.Button(
            frame,
            text="Add Item",
            command=self.add_item
        ).grid(
            row=1,
            column=5,
            padx=15,
            pady=5
        )

    def create_table(self):
        table_frame = ttk.Frame(self.root)
        table_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=10
        )

        columns = (
            "description",
            "quantity",
            "rate",
            "taxable",
            "gst_rate",
            "gst",
            "total"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.tree.heading(
            "description",
            text="Description"
        )
        self.tree.heading(
            "quantity",
            text="Qty"
        )
        self.tree.heading(
            "rate",
            text="Rate"
        )
        self.tree.heading(
            "taxable",
            text="Taxable Value"
        )
        self.tree.heading(
            "gst_rate",
            text="GST %"
        )
        self.tree.heading(
            "gst",
            text="GST Amount"
        )
        self.tree.heading(
            "total",
            text="Total"
        )

        self.tree.column(
            "description",
            width=180
        )
        self.tree.column(
            "quantity",
            width=70,
            anchor="center"
        )
        self.tree.column(
            "rate",
            width=110,
            anchor="e"
        )
        self.tree.column(
            "taxable",
            width=130,
            anchor="e"
        )
        self.tree.column(
            "gst_rate",
            width=80,
            anchor="center"
        )
        self.tree.column(
            "gst",
            width=120,
            anchor="e"
        )
        self.tree.column(
            "total",
            width=130,
            anchor="e"
        )

        self.tree.pack(
            fill="both",
            expand=True
        )

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=5)

        ttk.Button(
            button_frame,
            text="Remove Selected Item",
            command=self.remove_item
        ).grid(
            row=0,
            column=0,
            padx=10
        )

        ttk.Button(
            button_frame,
            text="Clear Invoice",
            command=self.clear_invoice
        ).grid(
            row=0,
            column=1,
            padx=10
        )

    def create_summary(self):
        summary_frame = ttk.LabelFrame(
            self.root,
            text="Invoice Summary",
            padding=15
        )
        summary_frame.pack(
            fill="x",
            padx=25,
            pady=(5, 20)
        )

        self.summary_label = tk.Label(
            summary_frame,
            text=self.get_empty_summary(),
            font=("Courier New", 11),
            justify="left"
        )

        self.summary_label.pack(
            anchor="e"
        )

    def get_empty_summary(self):
        return (
            "Taxable Value : Rs. 0.00\n"
            "Total GST     : Rs. 0.00\n"
            "Grand Total   : Rs. 0.00"
        )

    def add_item(self):
        description = self.description_entry.get().strip()

        if not description:
            messagebox.showerror(
                "Missing Description",
                "Please enter an item description."
            )
            return

        try:
            quantity = float(
                self.quantity_entry.get()
            )
            rate = float(
                self.rate_entry.get()
            )
            gst_rate = float(
                self.gst_var.get()
            )

            if quantity <= 0 or rate < 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Enter a valid quantity and rate."
            )
            return

        taxable_value = quantity * rate
        gst_amount = (
            taxable_value * gst_rate / 100
        )
        total = taxable_value + gst_amount

        item = {
            "description": description,
            "quantity": quantity,
            "rate": rate,
            "taxable": taxable_value,
            "gst_rate": gst_rate,
            "gst": gst_amount,
            "total": total
        }

        self.items.append(item)

        self.tree.insert(
            "",
            "end",
            values=(
                description,
                f"{quantity:g}",
                f"{rate:,.2f}",
                f"{taxable_value:,.2f}",
                f"{gst_rate:g}%",
                f"{gst_amount:,.2f}",
                f"{total:,.2f}"
            )
        )

        self.update_summary()
        self.clear_item_inputs()

    def update_summary(self):
        taxable_total = sum(
            item["taxable"]
            for item in self.items
        )

        gst_total = sum(
            item["gst"]
            for item in self.items
        )

        grand_total = (
            taxable_total + gst_total
        )

        transaction = (
            self.transaction_var.get()
        )

        if transaction == "Intra-State":
            cgst = gst_total / 2
            sgst = gst_total / 2

            summary = (
                f"Taxable Value : Rs. "
                f"{taxable_total:,.2f}\n"
                f"CGST          : Rs. "
                f"{cgst:,.2f}\n"
                f"SGST          : Rs. "
                f"{sgst:,.2f}\n"
                f"Total GST     : Rs. "
                f"{gst_total:,.2f}\n"
                f"Grand Total   : Rs. "
                f"{grand_total:,.2f}"
            )

        else:
            summary = (
                f"Taxable Value : Rs. "
                f"{taxable_total:,.2f}\n"
                f"IGST          : Rs. "
                f"{gst_total:,.2f}\n"
                f"Total GST     : Rs. "
                f"{gst_total:,.2f}\n"
                f"Grand Total   : Rs. "
                f"{grand_total:,.2f}"
            )

        self.summary_label.config(
            text=summary
        )

    def remove_item(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Select an item to remove."
            )
            return

        for selected_item in selected:
            index = self.tree.index(
                selected_item
            )

            self.tree.delete(
                selected_item
            )

            del self.items[index]

        self.update_summary()

    def clear_invoice(self):
        if not self.items:
            return

        confirm = messagebox.askyesno(
            "Clear Invoice",
            "Do you want to remove all items?"
        )

        if not confirm:
            return

        for row in self.tree.get_children():
            self.tree.delete(row)

        self.items.clear()

        self.summary_label.config(
            text=self.get_empty_summary()
        )

    def clear_item_inputs(self):
        self.description_entry.delete(
            0,
            tk.END
        )
        self.quantity_entry.delete(
            0,
            tk.END
        )
        self.rate_entry.delete(
            0,
            tk.END
        )

        self.description_entry.focus()


if __name__ == "__main__":
    root = tk.Tk()

    app = GSTInvoiceCalculator(root)

    root.mainloop()
