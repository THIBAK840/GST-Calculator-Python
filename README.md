## Project Preview

![GST Invoice Calculator](gst-calculator-screenshot.png)# GST Calculator & Invoice System – Python

A Python-based GST Calculator and Invoice System developed to calculate GST for Indian transactions.

The project combines my knowledge of **Python programming, accounting, taxation, and GST** to create a practical financial application.

## Features

- Calculate GST based on taxable value
- Supports 5%, 12%, 18%, and 28% GST rates
- Intra-State transactions with CGST and SGST
- Inter-State transactions with IGST
- Multiple invoice items
- Quantity × Rate calculation
- Automatic taxable value calculation
- Automatic GST calculation
- Invoice grand total
- Add and remove invoice items
- Clear invoice functionality
- Graphical User Interface using Tkinter
- Input validation for incorrect values

## Project Versions

### 1. Basic GST Calculator
File: `gst_calculator.py`

A command-line GST calculator that calculates CGST, SGST, IGST, total GST, and grand total.

### 2. GUI GST Calculator
File: `gst_calculator_gui.py`

A graphical version developed using Python Tkinter with input fields, GST rate selection, transaction type selection, and automatic GST calculation.

### 3. GST Invoice Calculator
File: `gst_invoice_calculator.py`

An advanced multi-item invoice calculator that supports:

- Item descriptions
- Quantity and rate
- Different GST rates
- Multiple invoice items
- CGST and SGST
- IGST
- Invoice totals

## GST Calculation Logic

### Intra-State Transaction

For transactions within the same state:

Total GST = Taxable Value × GST Rate / 100

CGST = Total GST / 2

SGST = Total GST / 2

Grand Total = Taxable Value + Total GST

### Inter-State Transaction

For transactions between different states:

IGST = Taxable Value × GST Rate / 100

Grand Total = Taxable Value + IGST

## Example

For a taxable value of Rs. 10,000 with 18% GST:

Total GST = Rs. 1,800

For an Intra-State transaction:

- CGST @ 9% = Rs. 900
- SGST @ 9% = Rs. 900
- Grand Total = Rs. 11,800

For an Inter-State transaction:

- IGST @ 18% = Rs. 1,800
- Grand Total = Rs. 11,800

## Technologies Used

- Python
- Tkinter
- Git
- GitHub

## How to Run

Make sure Python is installed on your computer.

Download or clone this repository.

Run the advanced GST Invoice Calculator:

```bash
python gst_invoice_calculator.py
