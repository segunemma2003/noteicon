import tkinter as tk
from forex_python.converter import CurrencyRates

def convert_currency():
    try:
        amount = float(entry_amount.get())
    except ValueError:
        result_label.config(text="Invalid input. Please enter a numeric value.")
        return
    
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    
    result_label.config(text="Converted Amount: {:.2f} {}".format(converted_amount, to_currency))

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Set the window size (width x height)
root.geometry("400x300")  # Adjust the dimensions as needed

# Label for the entry field
entry_label = tk.Label(root, text="Enter Amount:")
entry_label.pack()

# Entry field for amount
entry_amount = tk.Entry(root)
entry_amount.pack()

# Label for "From" currency
from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.pack()

# Dropdown menu for "From" currency
from_currency_var = tk.StringVar()
from_currency_var.set("USD")  # Set the default value
from_currency_menu = tk.OptionMenu(root, from_currency_var, "USD", "EUR", "GBP")
from_currency_menu.pack()

# Label for "To" currency
to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.pack()

# Dropdown menu for "To" currency
to_currency_var = tk.StringVar()
to_currency_var.set("EUR")  # Set the default value
to_currency_menu = tk.OptionMenu(root, to_currency_var, "USD", "EUR", "GBP")
to_currency_menu.pack()

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack()

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Prevent window resizing
root.resizable(False, False)

# Start the Tkinter main loop
root.mainloop()
