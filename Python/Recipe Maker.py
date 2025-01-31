import tkinter as tk
import tkinter.ttk as combobox


def create_recipe():
    name = nameinput.get()
    nameinput.delete(0, tk.END)
    recipe_type = recipe_combobox.get()
    recipe_combobox.set("")
    ingredients = []

    if ingredient1var.get() == 1:
        ingredients.append("Tomatoes")
    if ingredient2var.get() == 1:
        ingredients.append("Onions")
    if ingredient3var.get() == 1:
        ingredients.append("Garlic")
    if ingredient4var.get() == 1:
        ingredients.append("Cheese")

    ingredients_list = ", ".join(ingredients) if ingredients else "No ingredients selected"

    comment_text = comment_area.get("1.0", 'end-1c').strip()
    comment_area.delete("1.0", tk.END)

    result_label.config(
        text=f"Recipe created by {name}:\nType: {recipe_type}\nIngredients: {ingredients_list}\nComment: {comment_text}")


# Main window
window = tk.Tk()
window.title("Simple Recipe Creator")
window.geometry("400x400")

# User input fields
name_label = tk.Label(window, text="Your Name:")
nameinput = tk.Entry(window)

recipe_label = tk.Label(window, text="Select Recipe Type:")
recipe_combobox = combobox.Combobox(window, state="readonly", values=["Salad", "Pasta", "Soup", "Pizza"])
recipe_combobox.current(0)  # Default to first item

ingredients_label = tk.Label(window, text="Select Ingredients:")
ingredient1var = tk.IntVar()
ingredient2var = tk.IntVar()
ingredient3var = tk.IntVar()
ingredient4var = tk.IntVar()

ingredient1 = tk.Checkbutton(window, text="Tomatoes", variable=ingredient1var)
ingredient2 = tk.Checkbutton(window, text="Onions", variable=ingredient2var)
ingredient3 = tk.Checkbutton(window, text="Garlic", variable=ingredient3var)
ingredient4 = tk.Checkbutton(window, text="Cheese", variable=ingredient4var)

comment_label = tk.Label(window, text="Add a Comment:")
comment_area = tk.Text(window, height=3, width=30)

# Result display
result_label = tk.Label(window, text="", wraplength=300)

# Create Recipe button
create_button = tk.Button(window, text="Create Recipe", command=create_recipe)

# Layout
name_label.pack(pady=5)
nameinput.pack(pady=5)
recipe_label.pack(pady=5)
recipe_combobox.pack(pady=5)
ingredients_label.pack(pady=5)
ingredient1.pack(pady=2)
ingredient2.pack(pady=2)
ingredient3.pack(pady=2)
ingredient4.pack(pady=2)
comment_label.pack(pady=5)
comment_area.pack(pady=5)
create_button.pack(pady=10)
result_label.pack(pady=10)

window.mainloop()
