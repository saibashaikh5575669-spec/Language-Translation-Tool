import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator


def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    source = source_language.get()
    target = target_language.get()

    try:
        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror(
            "Error",
            "Translation failed. Please check your internet connection."
        )


def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


# Main window
root = tk.Tk()
root.title("AI Language Translation Tool")
root.geometry("700x600")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="🌐 AI Language Translation Tool",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)

# Language frame
language_frame = tk.Frame(root)
language_frame.pack(pady=10)

# Source language
tk.Label(
    language_frame,
    text="Source Language:",
    font=("Arial", 12, "bold")
).grid(row=0, column=0, padx=10)

source_language = ttk.Combobox(
    language_frame,
    values=["auto", "en", "hi", "mr", "gu", "ta", "te", "fr", "de", "es"],
    width=12,
    state="readonly"
)
source_language.set("auto")
source_language.grid(row=0, column=1, padx=10)

# Target language
tk.Label(
    language_frame,
    text="Target Language:",
    font=("Arial", 12, "bold")
).grid(row=0, column=2, padx=10)

target_language = ttk.Combobox(
    language_frame,
    values=["en", "hi", "mr", "gu", "ta", "te", "fr", "de", "es"],
    width=12,
    state="readonly"
)
target_language.set("hi")
target_language.grid(row=0, column=3, padx=10)

# Input
tk.Label(
    root,
    text="Enter Text:",
    font=("Arial", 13, "bold")
).pack(pady=(20, 5))

input_text = tk.Text(
    root,
    height=7,
    width=70,
    font=("Arial", 12)
)
input_text.pack()

# Translate button
translate_button = tk.Button(
    root,
    text="Translate",
    font=("Arial", 12, "bold"),
    command=translate_text,
    padx=20,
    pady=8
)
translate_button.pack(pady=15)

# Output
tk.Label(
    root,
    text="Translated Text:",
    font=("Arial", 13, "bold")
).pack(pady=(5, 5))

output_text = tk.Text(
    root,
    height=7,
    width=70,
    font=("Arial", 12)
)
output_text.pack()

# Clear button
clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial", 11),
    command=clear_text,
    padx=20
    pady=5
)
clear_button.pack(pady=15)

root.mainloop()