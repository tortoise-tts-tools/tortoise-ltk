import tkinter as tk
from tkinter import messagebox
from tokenizer import VoiceBpeTokenizer

# Create an instance of the tokenizer
tokenizer = VoiceBpeTokenizer()

# Function to calculate and display the token count
def calculate_token_count(*args):
    input_text = text_var.get().strip()
    tokens = tokenizer.encode(input_text)
    token_count = len(tokens)
    token_count_label.config(text=f"Token Count: {token_count}")

    # Change text color based on length
    if len(input_text) >= 400:
        text_entry.configure(foreground="red")
    elif len(input_text) > 350:
        text_entry.configure(foreground="orange")
    else:
        text_entry.configure(foreground="black")

# Create the main window
window = tk.Tk()
window.title("Token Count")
window.geometry("300x200")

# Create a text entry field
text_var = tk.StringVar()
text_entry = tk.Entry(window, textvariable=text_var)
text_entry.pack()

# Create a label to display the token count
token_count_label = tk.Label(window, text="Token Count: 0")
token_count_label.pack()

# Attach the callback function to the text entry variable
text_var.trace_add("write", calculate_token_count)

# Start the GUI event loop
window.mainloop()
