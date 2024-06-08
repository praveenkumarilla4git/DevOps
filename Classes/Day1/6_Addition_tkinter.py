import tkinter as tk
from tkinter import simpledialog

base = tk.Tk()

base.withdraw()

num1 = float(simpledialog.askstring("Input", "Ener the first number:"))

num2 = float(simpledialog.askstring("Input", "Ener the second number:"))

sum_result = num1 + num2

print("The sum is:", sum_result)



