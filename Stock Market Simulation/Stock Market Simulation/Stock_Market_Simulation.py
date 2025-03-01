import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib as plt

stock1 = pd.read_csv("C:\\Users\\tommy\\Downloads\\Stock Market Dataset\\Stocks\\wrd_us.txt", sep = ',')



def greet_user():
    username = entry_name.get()
    if username.strip():
        messagebox.showinfo("Greet", f"Hello, {username}!")
    else:
        messagebox.showwarning("Greet", "Please enter a name.")

main_root = tk.Tk()

main_root.geometry('1920x1080')
main_root.title("Stock Market Simulation")

"""
# Create a label and entry in a frame
frame_input = tk.Frame(root)
frame_input.pack(pady=10)  # Add some vertical padding

label_name = tk.Label(frame_input, text="Enter your name:")
label_name.grid(row=0, column=0, padx=5, pady=5)

entry_name = tk.Entry(frame_input)
entry_name.grid(row=0, column=1, padx=5, pady=5)

# Create a button in another frame
frame_button = tk.Frame(root)
frame_button.pack()

button_greet = tk.Button(frame_button, text="Greet", command=greet_user)
button_greet.pack(padx=5, pady=5)
print(stock1.head())

"""
def show_stocks(df):
    root = tk.Toplevel()
    root.title('Stocks')
    tree = ttk.Treeview(root)
    tree['columns'] = list(df.columns)
    for col in df.columns:
        tree.heading(col, text = col)
        tree.column(col, anchor = 'w')
    for _, row in df.iterrows():
        tree.insert('', 'end', values = list(row))
    tree.pack(expand = True, fill = 'both')


show_button = tk.Button(main_root, text = "Show Stock 1", command = lambda: show_stocks(stock1))
show_button.pack(pady = 20, padx = 15)
main_root.mainloop()
