import tkinter as tk
import tkinter.ttk as combobox
import tkinter.messagebox as msgbox


def input_data():
    if (inpt_name.get() != "" and inpt_color.get() != ""
            and inpt_power.get() != "" and inpt_size.get() != ""
            and inpt_age.get() != ""):

        monster_list.append(inpt_name.get())
        color_list.append(inpt_color.get())
        power_list.append(inpt_power.get())
        size_list.append(inpt_size.get())
        age_list.append(inpt_age.get())

        traits = []
        if trait_friendly_var.get():
            traits.append("Friendly")
        if trait_timid_var.get():
            traits.append("Timid")
        if trait_aggressive_var.get():
            traits.append("Aggressive")

        is_friendly_list.append(", ".join(traits) if traits else "No traits selected")

        # Clear input fields
        inpt_name.delete(0, tk.END)
        inpt_color.delete(0, tk.END)
        inpt_power.delete(0, tk.END)
        inpt_size.set("")
        inpt_age.delete(0, tk.END)
        inpt_age.insert(0, 0)  # Reset spinner to 0
        trait_friendly_var.set(False)  # Uncheck the checkbox
        trait_timid_var.set(False)  # Uncheck the checkbox
        trait_aggressive_var.set(False)  # Uncheck the checkbox
    else:
        msgbox.showwarning("Warning", "Every field must be filled to input data.")


def view_list():
    list_window = tk.Toplevel(window)
    list_window.title("Monster Profiles")
    list_window.geometry("500x400")

    headers = ["MONSTER NAME", "COLOR", "POWER", "SIZE", "AGE", "TRAITS"]
    for idx, header in enumerate(headers):
        header_label = tk.Label(list_window, text=header)
        header_label.grid(column=idx, row=0)

    for i in range(len(monster_list)):
        name_label = tk.Label(list_window, text=monster_list[i])
        color_label = tk.Label(list_window, text=color_list[i])
        power_label = tk.Label(list_window, text=power_list[i])
        size_label = tk.Label(list_window, text=size_list[i])
        age_label = tk.Label(list_window, text=age_list[i])
        traits_label = tk.Label(list_window, text=is_friendly_list[i])

        name_label.grid(column=0, row=i + 1)
        color_label.grid(column=1, row=i + 1)
        power_label.grid(column=2, row=i + 1)
        size_label.grid(column=3, row=i + 1)
        age_label.grid(column=4, row=i + 1)
        traits_label.grid(column=5, row=i + 1)


def clear_list():
    if monster_list:
        choice = msgbox.askyesno("Warning", "You are going to delete the content of your list. Proceed?")
        if choice:
            monster_list.clear()
            color_list.clear()
            power_list.clear()
            size_list.clear()
            age_list.clear()
            is_friendly_list.clear()
            msgbox.showinfo("Notice", "Your monster profiles are now empty.")
    else:
        msgbox.showinfo("Notice", "Your list is already empty.")


def show_credits():
    credit_win = tk.Toplevel(window)
    credit_win.title("Credits")
    credit_win.geometry("400x100")
    credit_label = tk.Label(credit_win, text="Created with love for monster fans!")
    credit_label.pack()


def show_version():
    version_win = tk.Toplevel(window)
    version_win.title("Version")
    version_win.geometry("200x100")
    version_label = tk.Label(version_win, text="Current software version: 1.0")
    version_label.pack()


# Data Lists
monster_list = []
color_list = []
power_list = []
size_list = []
age_list = []
is_friendly_list = []

# Main Window
window = tk.Tk()
window.title("Monster Profile Creator")
window.geometry("500x400")

# UI Elements
lbl_title = tk.Label(window, text="Welcome to the Monster Profile Creator!")
lbl_desc = tk.Label(window, text="Create your own monster profiles.")
lbl_name = tk.Label(window, text="Monster Name:")
lbl_color = tk.Label(window, text="Monster Color:")
lbl_power = tk.Label(window, text="Special Power:")
lbl_size = tk.Label(window, text="Size:")
lbl_age = tk.Label(window, text="Age:")
lbl_traits = tk.Label(window, text="Traits:")

inpt_name = tk.Entry(window, width=20)
inpt_color = tk.Entry(window, width=20)
inpt_power = tk.Entry(window, width=20)

# ComboBox for size
sizes = ("Tiny", "Small", "Medium", "Large", "Gigantic")
inpt_size = combobox.Combobox(window, width=20, values=sizes, state="readonly")
inpt_size.set("")  # Set default value

# Spinner for age
inpt_age = tk.Spinbox(window, from_=0, to=100, width=5)

# Checkboxes for traits
trait_friendly_var = tk.BooleanVar()
trait_friendly = tk.Checkbutton(window, text="Friendly", variable=trait_friendly_var)

trait_timid_var = tk.BooleanVar()
trait_timid = tk.Checkbutton(window, text="Timid", variable=trait_timid_var)

trait_aggressive_var = tk.BooleanVar()
trait_aggressive = tk.Checkbutton(window, text="Aggressive", variable=trait_aggressive_var)

inpt_btn = tk.Button(window, text="Create Monster", command=input_data)

# Layout
lbl_title.grid(row=0, column=0, columnspan=2, sticky=tk.E + tk.W)
lbl_desc.grid(row=1, column=0, columnspan=2, sticky=tk.E + tk.W)
lbl_name.grid(row=2, column=0)
inpt_name.grid(row=2, column=1, sticky=tk.W)
lbl_color.grid(row=3, column=0)
inpt_color.grid(row=3, column=1, sticky=tk.W)
lbl_power.grid(row=4, column=0)
inpt_power.grid(row=4, column=1, sticky=tk.W)
lbl_size.grid(row=5, column=0)
inpt_size.grid(row=5, column=1, sticky=tk.W)
lbl_age.grid(row=6, column=0)
inpt_age.grid(row=6, column=1, sticky=tk.W)
lbl_traits.grid(row=7, column=0)
trait_friendly.grid(row=8, column=0)
trait_timid.grid(row=8, column=1)
trait_aggressive.grid(row=8, column=2)
inpt_btn.grid(row=9, column=0)

# Menu Bar
menubar = tk.Menu(window)

list_menu = tk.Menu(menubar, tearoff=0)
list_menu.add_command(label="View Profiles", command=view_list)
list_menu.add_separator()
list_menu.add_command(label="Clear Profiles", command=clear_list)
menubar.add_cascade(label="Profile Options", menu=list_menu)

menubar.add_command(label="Credits", command=show_credits)
menubar.add_command(label="Version", command=show_version)

window.config(menu=menubar)
window.mainloop()
