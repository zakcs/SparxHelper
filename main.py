import tkinter as tk
from tkinter import ttk
import json
import random
import sys

errorFinding = ["cant find that mate", "are u sure that exists??", "nope cant find it", "bookwork code not found im afraid", "i dont think you've saved that"]

def save_answer():
    # Get the bookwork code and answer from the entries
    bookwork_code = bookwork_code_entry.get().lower()
    answer = answer_entry.get()

    # Load the existing data from the json file
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except:
        data = {}

    # Add the new bookwork code and answer to the data
    data[bookwork_code] = answer

    # Save the data to the json file
    with open('data.json', 'w') as f:
        json.dump(data, f)
    bookwork_code_entry.delete(0, tk.END)
    answer_entry.delete(0, tk.END)
    status_label.config(text="ur answer saved!!!!!!!")

def recall_answer():
    # Get the bookwork code from the entry
    bookwork_code = recall_entry.get().lower()

    # Load the data from the json file
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Get the answer for the bookwork code
    answer = data.get(bookwork_code, f'{random.choice(errorFinding)}')

    # Display the answer in the label
    recall_label.config(text=answer, font=("Helvetica", 16))
    recall_entry.delete(0, tk.END)
    status_label.config(text="yay")

root = tk.Tk()
root.wm_iconbitmap(default=sys._MEIPASS + '\\myicon.ico')
root.title("sparx thingy")

# Create a main frame to hold the widgets
mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Create the widgets
bookwork_code_label = ttk.Label(mainframe, text="bookwork code:")
bookwork_code_entry = ttk.Entry(mainframe)
answer_label = ttk.Label(mainframe, text="answer:")
answer_entry = ttk.Entry(mainframe)
save_button = ttk.Button(mainframe, text="save", command=save_answer)
recall_label = ttk.Label(mainframe, text="")
recall_entry = ttk.Entry(mainframe)
recall_button = ttk.Button(mainframe, text="get ur answer lol", command=recall_answer)
status_label = ttk.Label(mainframe, text="")
title_label = ttk.Label(mainframe, text="welcome to zaks cool sparx helpy thingy", font=("Helvetica", 16), foreground="red")

# Position the widgets in the main frame
title_label.grid(column=0, row=0, columnspan=2, pady=10)
bookwork_code_label.grid(column=0, row=1, sticky=tk.W)
bookwork_code_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))
answer_label.grid(column=0, row=2, sticky=tk.W)
answer_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))
save_button.grid(column=1, row=3, sticky=tk.E)
recall_entry.grid(column=0, row=4, sticky=(tk.W, tk.E))
recall_button.grid(column=1, row=4, sticky=tk.E)
recall_label.grid(column=0, row=5, columnspan=2, sticky=(tk.W, tk.E))
status_label.grid(column=0, row=6, columnspan=2, sticky=(tk.W, tk.E))

# Add padding to the widgets
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

# Set focus on the bookwork code entry
bookwork_code_entry.focus()

root.mainloop()
