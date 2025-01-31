import tkinter as tk
import googletrans
from tkinter import ttk, messagebox

window = tk.Tk()
window.title("Kodingnext - Translator")
window.geometry("880x400")


# Function
def translate_it():
    # Delete Any Previous Translations
    translated_text.delete("1.0", "end-1c")

    # Get the original text
    original = original_text.get("1.0", "end-1c").strip()

    # Check if the input fields and combo boxes are filled
    if not original or not original_combo.get() or not translated_combo.get():
        messagebox.showerror("Translator", "Please fill the entry fields or combobox")
        return  # Exit the function if input is not valid

    try:
        # Get the From Language Key
        from_language_key = next((key for key, value in languages.items() if value == original_combo.get()), None)

        # Get the To Language Key
        to_language_key = next((key for key, value in languages.items() if value == translated_combo.get()), None)

        # Create a Translator object
        translator = googletrans.Translator()

        # Translate Text
        translated = translator.translate(original, src=from_language_key, dest=to_language_key)

        # Output translated text to screen
        translated_text.insert(1.0, translated.text)

    except Exception as e:
        messagebox.showerror("Translator", f"An error occurred: {e}")


def clear():
    # Clear the text boxes
    original_text.delete("1.0", "end-1c")
    translated_text.delete("1.0", "end-1c")


# Widget
lbl1 = tk.Label(window, text="Your Translator", font=("calibri", 20))
original_text = tk.Text(window, height=10, width=40)
translated_text = tk.Text(window, height=10, width=40)

# Grab Language List From GoogleTrans
languages = googletrans.LANGUAGES

# Convert to list
language_list = list(languages.values())
# Combo boxes
original_combo = ttk.Combobox(window, width=50, state="readonly", value=language_list)
translated_combo = ttk.Combobox(window, width=50, state="readonly", value=language_list)

translate_button = tk.Button(window, text="Translate!", font=("Helvetica", 24), command=translate_it)
clear_button = tk.Button(window, text="Clear", font=("Helvetica", 24), command=clear)

# Placement
lbl1.grid(row=0, column=1)
original_text.grid(row=2, column=0, pady=20, padx=10)
translated_text.grid(row=2, column=2, pady=20, padx=10)
translated_combo.grid(row=1, column=2)
original_combo.grid(row=1, column=0)
translate_button.grid(row=3, column=0, padx=10)
clear_button.grid(row=3, column=1, rowspan=100, columnspan=20)

window.mainloop()
