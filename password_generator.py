import random
import string
import pyperclip
from tkinter import *

# Initialize window
root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Enhanced Password Generator")

# Heading
heading = Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
Label(root, text='Create secure passwords', font='arial 10').pack(pady=5)

# Select password length
Label(root, text='PASSWORD LENGTH', font='arial 10 bold').pack(pady=5)
pass_len = IntVar(value=12)
Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()

# Options to include/exclude special characters and digits
include_special = IntVar(value=1)
include_digits = IntVar(value=1)

Checkbutton(root, text="Include Special Characters", variable=include_special).pack(pady=5)
Checkbutton(root, text="Include Digits", variable=include_digits).pack(pady=5)

# Define function
pass_str = StringVar()

def Generator():
    char_set = string.ascii_letters
    if include_digits.get():
        char_set += string.digits
    if include_special.get():
        char_set += string.punctuation

    password = ''.join(random.choice(char_set) for _ in range(pass_len.get()))
    pass_str.set(password)

# Generate Password Button
Button(root, text="GENERATE PASSWORD", command=Generator).pack(pady=10)

# Display the generated password
Entry(root, textvariable=pass_str, width=35, font='arial 12').pack(pady=5)

# Function to copy the password to clipboard
def Copy_password():
    pyperclip.copy(pass_str.get())

# Copy to Clipboard Button
Button(root, text='COPY TO CLIPBOARD', command=Copy_password).pack(pady=10)

# Loop to run program
root.mainloop()
