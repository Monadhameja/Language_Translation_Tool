import tkinter as tk
from tkinter import ttk
from translator import Translator

translator = Translator()

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Russian": "ru",
    "Arabic": "ar",
    "Italian": "it"
}

root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("700x550")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

input_box = tk.Text(
    root,
    height=8,
    width=70
)

input_box.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

source_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    width=20
)

source_lang.current(0)
source_lang.grid(row=0, column=0, padx=10)

target_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    width=20
)

target_lang.current(1)
target_lang.grid(row=0, column=1, padx=10)


def translate_text():

    text = input_box.get("1.0", tk.END).strip()

    if text == "":
        return

    translated = translator.translate(
        text,
        languages[source_lang.get()],
        languages[target_lang.get()]
    )

    output_box.delete("1.0", tk.END)

    output_box.insert(tk.END, translated)


button = tk.Button(
    root,
    text="Translate",
    command=translate_text,
    bg="blue",
    fg="white",
    width=20
)

button.pack(pady=15)

output_box = tk.Text(
    root,
    height=8,
    width=70
)

output_box.pack()

root.mainloop()