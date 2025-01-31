import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Calculator by Matthew")
window.resizable(0, 0)
window.geometry('350x500')

expression = ""
memory = 0  # Variable to store memory value

def insert_number(number):
    global expression
    expression += str(number)
    input_text.set(expression)

def button_clear():
    global expression
    expression = ""
    input_text.set("")

def result():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
        button_clear()
    except Exception as e:
        messagebox.showerror("Error", "Invalid input.")
        button_clear()

def memory_add():
    global memory
    try:
        memory += float(input_text.get())
        messagebox.showinfo("Memory", "Value added to memory.")
    except ValueError:
        messagebox.showerror("Error", "No valid number to add.")

def memory_subtract():
    global memory
    try:
        memory -= float(input_text.get())
        messagebox.showinfo("Memory", "Value subtracted from memory.")
    except ValueError:
        messagebox.showerror("Error", "No valid number to subtract.")

def memory_recall():
    global memory
    input_text.set(memory)

def percentage():
    global expression
    try:
        result = str(eval(expression))  # Evaluate the current expression
        input_text.set(float(result) / 100)  # Set the entry to the percentage
        expression = str(float(result) / 100)  # Update expression
    except Exception as e:
        messagebox.showerror("Error", "Invalid input.")
        button_clear()

input_text = tk.StringVar()

# Entry input
entry = tk.Entry(window, width=18, borderwidth=5, font=("Arial", 24), textvariable=input_text, justify="right", bg='white', fg='black')

# Button numbers
button_1 = tk.Button(window, text="1", padx=20, pady=20, command=lambda: insert_number(1), bg='yellow', fg='black', font=("Arial", 18))
button_2 = tk.Button(window, text="2", padx=20, pady=20, command=lambda: insert_number(2), bg='yellow', fg='black', font=("Arial", 18))
button_3 = tk.Button(window, text="3", padx=20, pady=20, command=lambda: insert_number(3), bg='yellow', fg='black', font=("Arial", 18))
button_4 = tk.Button(window, text="4", padx=20, pady=20, command=lambda: insert_number(4), bg='yellow', fg='black', font=("Arial", 18))
button_5 = tk.Button(window, text="5", padx=20, pady=20, command=lambda: insert_number(5), bg='yellow', fg='black', font=("Arial", 18))
button_6 = tk.Button(window, text="6", padx=20, pady=20, command=lambda: insert_number(6), bg='yellow', fg='black', font=("Arial", 18))
button_7 = tk.Button(window, text="7", padx=20, pady=20, command=lambda: insert_number(7), bg='yellow', fg='black', font=("Arial", 18))
button_8 = tk.Button(window, text="8", padx=20, pady=20, command=lambda: insert_number(8), bg='yellow', fg='black', font=("Arial", 18))
button_9 = tk.Button(window, text="9", padx=20, pady=20, command=lambda: insert_number(9), bg='yellow', fg='black', font=("Arial", 18))
button_0 = tk.Button(window, text="0", padx=20, pady=20, command=lambda: insert_number(0), bg='yellow', fg='black', font=("Arial", 18))
button_add = tk.Button(window, text="+", padx=22, pady=20, command=lambda: insert_number('+'), bg='orange', fg='black', font=("Arial", 18))
button_subtraction = tk.Button(window, text="-", padx=24, pady=20, command=lambda: insert_number('-'), bg='orange', fg='black', font=("Arial", 18))
button_multiplication = tk.Button(window, text="*", padx=24, pady=20, command=lambda: insert_number('*'), bg='orange', fg='black', font=("Arial", 18))
button_division = tk.Button(window, text="/", padx=24, pady=20, command=lambda: insert_number('/'), bg='orange', fg='black', font=("Arial", 18))
button_equal = tk.Button(window, text="=", padx=20, pady=20, command=result, bg='green', fg='black', font=("Arial", 18))
button_clear = tk.Button(window, text="Clear", command=button_clear, padx=10, pady=20, bg='red', fg='white', font=("Arial", 18))

# Memory buttons
button_memory_add = tk.Button(window, text="M+", command=memory_add, padx=10, pady=10, bg='lightgray', fg='black', font=("Arial", 12))
button_memory_subtract = tk.Button(window, text="M-", command=memory_subtract, padx=10, pady=10, bg='lightgray', fg='black', font=("Arial", 12))
button_memory_recall = tk.Button(window, text="MR", command=memory_recall, padx=10, pady=10, bg='lightgray', fg='black', font=("Arial", 12))

# Percentage button
button_percentage = tk.Button(window, text="%", command=percentage, padx=20, pady=20, bg='lightblue', fg='black', font=("Arial", 18))

# Button Place Grid
entry.grid(row=0, column=0, columnspan=4)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_add.grid(row=2, column=3)
button_subtraction.grid(row=1, column=3)
button_multiplication.grid(row=3, column=3)
button_division.grid(row=4, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=0)

# Memory buttons and percentage button
button_memory_add.grid(row=5, column=0)
button_memory_subtract.grid(row=5, column=1)
button_memory_recall.grid(row=5, column=2)
button_percentage.grid(row=5, column=3)

window.mainloop()
