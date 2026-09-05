import tkinter as tk
from validators import validate_name


def launch_ui():
    def show_name():
        name = name_entry.get()

        is_valid, message = validate_name(name)

        if not is_valid:
            result_label.config(
                text=message,
                fg="red"
            )
            return

        result_label.config(
            text=f"Hello, {name.strip()}!",
            fg="green"
        )

    root = tk.Tk()
    root.title("Name App")
    root.geometry("350x220")

    tk.Label(
        root,
        text="Enter Your Name",
        font=("Arial", 14)
    ).pack(pady=10)

    name_entry = tk.Entry(root, width=30)
    name_entry.pack(pady=10)

    tk.Button(
        root,
        text="Submit",
        command=show_name
    ).pack(pady=10)

    result_label = tk.Label(
        root,
        text="",
        font=("Arial", 11)
    )
    result_label.pack(pady=10)

    root.mainloop()
