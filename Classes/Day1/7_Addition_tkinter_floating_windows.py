import tkinter as tk
from tkinter import simpledialog, messagebox

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

def perform_addition():
    # Prompt the user to enter the first number using a dialog box
    num1 = float(simpledialog.askstring("Input", "Enter the first number:"))

    # Prompt the user to enter the second number using a dialog box
    num2 = float(simpledialog.askstring("Input", "Enter the second number:"))

    # Calculate the sum of the two numbers
    sum_result = num1 + num2

    # Display the result using a messagebox
    #messagebox.showinfo("Result", f"Result of addition of the given two numbers: {sum_result}")
    messagebox.showinfo("Result", f"Result of addition of the given two numbers: {sum_result}")

perform_addition()
root.mainloop()
