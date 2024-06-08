import tkinter as tk
from tkinter import messagebox

def perform_addition():
    # Create a new window for the addition dialog
    dialog = tk.Toplevel(root)
    dialog.title("Addition Dialog")

    # First number label and entry
    label1 = tk.Label(dialog, text="Enter the first number:")
    label1.pack(pady=5)
    entry1 = tk.Entry(dialog)
    entry1.pack(pady=5)

    # Second number label and entry
    label2 = tk.Label(dialog, text="Enter the second number:")
    label2.pack(pady=5)
    entry2 = tk.Entry(dialog)
    entry2.pack(pady=5)

    # Result label
    result_label = tk.Label(dialog, text="")
    result_label.pack(pady=10)

    def calculate_sum():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            sum_result = num1 + num2
            result_label.config(text=f"Result: {sum_result}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers")

    # Calculate button
    calculate_button = tk.Button(dialog, text="Calculate", command=calculate_sum)
    calculate_button.pack(pady=5)

    # Close window button
    close_button = tk.Button(dialog, text="Close", command=dialog.destroy)
    close_button.pack(pady=5)

# Main Tkinter root window
root = tk.Tk()
root.title("Main Window")
root.geometry("300x100")

# Button to open the addition dialog
open_dialog_button = tk.Button(root, text="Open Addition Dialog", command=perform_addition)
open_dialog_button.pack(pady=20)

root.mainloop()
