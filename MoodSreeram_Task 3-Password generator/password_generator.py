import tkinter as tk
from tkinter import messagebox
import string
import secrets
import pyperclip


# Generate a secure password
def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length.")
        return

    if length < 8:
        messagebox.showerror("Error", "Password length must be at least 8.")
        return

    selected_types = []

    if uppercase_var.get():
        selected_types.append(string.ascii_uppercase)

    if lowercase_var.get():
        selected_types.append(string.ascii_lowercase)

    if numbers_var.get():
        selected_types.append(string.digits)

    if symbols_var.get():
        selected_types.append(string.punctuation)

    if len(selected_types) < 2:
        messagebox.showerror(
            "Error",
            "Please select at least 2 character types."
        )
        return

    # Remove ambiguous characters if selected
    if ambiguous_var.get():
        ambiguous = "0O1lI"

        selected_types = [
            "".join(c for c in group if c not in ambiguous)
            for group in selected_types
        ]

    # Make sure every selected type contributes at least one character
    password = [
        secrets.choice(characters)
        for characters in selected_types
    ]

    all_characters = "".join(selected_types)

    # Fill remaining positions
    for _ in range(length - len(password)):
        password.append(secrets.choice(all_characters))

    # Securely shuffle password
    for i in range(len(password) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password[i], password[j] = password[j], password[i]

    final_password = "".join(password)

    password_var.set(final_password)

    # Copy automatically
    pyperclip.copy(final_password)

    # Add to history
    history.insert(0, final_password)

    if len(history) > 5:
        history.pop()

    update_history()
    update_strength(length, len(selected_types))


def update_strength(length, diversity):
    score = 0

    if length >= 12:
        score += 1

    if length >= 16:
        score += 1

    if diversity >= 3:
        score += 1

    if diversity == 4:
        score += 1

    if score <= 1:
        strength_var.set("Strength: Weak")
    elif score <= 2:
        strength_var.set("Strength: Medium")
    else:
        strength_var.set("Strength: Strong")


def update_history():
    history_text.delete("1.0", tk.END)

    for i, password in enumerate(history, 1):
        history_text.insert(tk.END, f"{i}. {password}\n")


def copy_password():
    password = password_var.get()

    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Generate a password first.")


# Main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("600x650")
root.resizable(False, False)

# Variables
length_var = tk.StringVar(value="16")
password_var = tk.StringVar()
strength_var = tk.StringVar(value="Strength: ")

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
ambiguous_var = tk.BooleanVar(value=False)

history = []


# Title
title = tk.Label(
    root,
    text="Random Password Generator",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)


# Length
tk.Label(
    root,
    text="Password Length (minimum 8):",
    font=("Arial", 12)
).pack()

tk.Spinbox(
    root,
    from_=8,
    to=100,
    textvariable=length_var,
    width=10,
    font=("Arial", 12)
).pack(pady=8)


# Character types
tk.Label(
    root,
    text="Select Character Types:",
    font=("Arial", 12, "bold")
).pack(pady=10)

tk.Checkbutton(
    root,
    text="Uppercase Letters (A-Z)",
    variable=uppercase_var,
    font=("Arial", 11)
).pack(anchor="w", padx=180)

tk.Checkbutton(
    root,
    text="Lowercase Letters (a-z)",
    variable=lowercase_var,
    font=("Arial", 11)
).pack(anchor="w", padx=180)

tk.Checkbutton(
    root,
    text="Numbers (0-9)",
    variable=numbers_var,
    font=("Arial", 11)
).pack(anchor="w", padx=180)

tk.Checkbutton(
    root,
    text="Symbols (!@#$...)",
    variable=symbols_var,
    font=("Arial", 11)
).pack(anchor="w", padx=180)


# Ambiguous characters
tk.Checkbutton(
    root,
    text="Exclude ambiguous characters (0, O, 1, l, I)",
    variable=ambiguous_var,
    font=("Arial", 11)
).pack(pady=10)


# Password display
tk.Label(
    root,
    text="Generated Password:",
    font=("Arial", 12, "bold")
).pack(pady=5)

tk.Entry(
    root,
    textvariable=password_var,
    width=48,
    font=("Arial", 13),
    justify="center"
).pack(pady=5)


# Strength
tk.Label(
    root,
    textvariable=strength_var,
    font=("Arial", 13, "bold")
).pack(pady=8)


# Buttons
tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 12, "bold"),
    padx=15,
    pady=8
).pack(pady=5)

tk.Button(
    root,
    text="Copy to Clipboard",
    command=copy_password,
    font=("Arial", 11),
    padx=15,
    pady=5
).pack(pady=5)


# History
tk.Label(
    root,
    text="Last 5 Generated Passwords",
    font=("Arial", 12, "bold")
).pack(pady=10)

history_text = tk.Text(
    root,
    height=6,
    width=55,
    font=("Consolas", 10)
)
history_text.pack()


root.mainloop()