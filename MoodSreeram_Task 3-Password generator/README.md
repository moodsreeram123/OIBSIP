# Random Password Generator

A simple desktop password generator built with Python and Tkinter. It creates secure random passwords using Python's `secrets` module and copies each generated password to the clipboard automatically.

## Features

- Choose a password length from 8 to 100 characters.
- Include uppercase letters, lowercase letters, numbers, and symbols.
- Exclude ambiguous characters such as `0`, `O`, `1`, `l`, and `I`.
- Ensure every selected character type is represented in the password.
- Display a strength rating: Weak, Medium, or Strong.
- Copy the generated password to the clipboard.
- Keep a history of the last five generated passwords.

## Requirements

- Python 3.8 or later
- Tkinter, usually included with Python
- `pyperclip`

Install the external dependency with:

```bash
pip install pyperclip
```

## Run the Application

From this folder, run:

```bash
python password_generator.py
```

## How to Use

1. Select a password length. The minimum length is 8 characters.
2. Select at least two character types.
3. Optionally enable ambiguous-character exclusion.
4. Select **Generate Password**.
5. Use **Copy to Clipboard** when you need to copy the displayed password.

Generated passwords are copied automatically after generation. The application keeps only the five most recent passwords in its in-memory history, which is cleared when the application closes.

## Validation

The application shows an error when:

- The password length is not a valid number.
- The password length is less than 8.
- Fewer than two character types are selected.

## Security

Passwords are generated with Python's cryptographically secure `secrets` module. Do not share generated passwords, and avoid storing them in plain text.

## Project File

| File | Description |
| --- | --- |
| `password_generator.py` | Tkinter application source code |
| `README.md` | Project documentation |
