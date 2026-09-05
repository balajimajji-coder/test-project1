import tkinter as tk


def show_name():
    name = name_entry.get().strip()

    if not name:
        result_label.config(
            text="Please enter your name.",
            fg="red"
        )
        return

    if len(name) < 2:
        result_label.config(
            text="Name must be at least 2 characters long.",
            fg="red"
        )
        return

    if not all(char.isalpha() or char.isspace() for char in name):
        result_label.config(
            text="Name can only contain letters and spaces.",
            fg="red"
        )
        return

    result_label.config(
        text=f"Hello, {name}!",
        fg="green"
    )


root = tk.Tk()
root.title("Name App")
root.geometry("350x220")

title_label = tk.Label(
    root,
    text="Enter Your Name",
    font=("Arial", 14)
)
title_label.pack(pady=10)

name_entry = tk.Entry(
    root,
    width=30
)
name_entry.pack(pady=10)

submit_button = tk.Button(
    root,
    text="Submit",
    command=show_name
)
submit_button.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 11)
)
result_label.pack(pady=10)

root.mainloop()
