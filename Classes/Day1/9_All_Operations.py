import tkinter as tk
from tkinter import messagebox


def perform_addition():
    perform_operation("Addition", "+")


def perform_subtraction():
    perform_operation("Subtraction", "-")


def perform_multiplication():
    perform_operation("Multiplication", "*")


def perform_division():
    perform_operation("Division", "/")


def perform_operation(operation_name, operator):
    dialog = tk.Toplevel(root)
    dialog.title(f"{operation_name} Dialog")

    label1 = tk.Label(dialog, text="Enter the first number:")
    label1.pack(pady=5)
    entry1 = tk.Entry(dialog)
    entry1.pack(pady=5)

    label2 = tk.Label(dialog, text="Enter the second number:")
    label2.pack(pady=5)
    entry2 = tk.Entry(dialog)
    entry2.pack(pady=5)

    result_label = tk.Label(dialog, text="")
    result_label.pack(pady=10)

    def calculate():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = num1 / num2

            result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers")
        except ZeroDivisionError as e:
            messagebox.showerror("Division Error", str(e))

    calculate_button = tk.Button(dialog, text="Calculate", command=calculate)
    calculate_button.pack(pady=5)

    close_button = tk.Button(dialog, text="Close", command=dialog.destroy)
    close_button.pack(pady=5)


# Main Tkinter root window
root = tk.Tk()
root.title("Operations Window")
root.geometry("300x250")

# Buttons to open each operation dialog
add_button = tk.Button(root, text="Addition", command=perform_addition)
add_button.pack(pady=5)

sub_button = tk.Button(root, text="Subtraction", command=perform_subtraction)
sub_button.pack(pady=5)

mul_button = tk.Button(root, text="Multiplication", command=perform_multiplication)
mul_button.pack(pady=5)

div_button = tk.Button(root, text="Division", command=perform_division)
div_button.pack(pady=5)

# Close button for the main window
close_main_button = tk.Button(root, text="Close", command=root.quit)
close_main_button.pack(pady=20)

root.mainloop()
