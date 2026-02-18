import tkinter as tk
from tkinter import messagebox

def generate_multiplication_table():
    table = []
    for i in range(1, 10):
        row = []
        for j in range(1, i + 1):
            result = i * j
            expression = f"{j}×{i}={result}"
            row.append(expression)
        table.append("  ".join(row))
    return "\n".join(table)

def show_multiplication_table():
    table = generate_multiplication_table()
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("乘法口诀表", table)
    root.destroy()

if __name__ == "__main__":
    show_multiplication_table()
