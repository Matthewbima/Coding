import tkinter as tk
import random

# Function to display results
def result():
    fname = fnameinput.get()
    nname = nnameinput.get()
    zodiac = zodiacvar.get()
    email = emailinput.get()
    password = passwordinput.get()
    gender = gendervar.get()
    if len(password) > 2:
        masked_password = password[0] + "*" * (len(password) - 2) + password[-1]
    else:
        masked_password = password
    datedob = date.get()
    modob = month.get()
    yeardob = year.get()
    getFortune = random.randint(1, 5)
    fortune = ""
    if getFortune == 1:
        fortune = "You're gonna be rich soon."
    elif getFortune == 2:
        fortune = "You're gonna meet your soulmate soon"
    elif getFortune == 3:
        fortune = "You're gonna be successful in the future"
    elif getFortune == 4:
        fortune = "You're gonna have 4 kids"
    elif getFortune == 5:
        fortune = "You're gonna undergo an unfortunate event soon."
    text1 = f"So, your name is {fname} and you wish to get your fortune told? \nYour friends and family call you {nname}\n"
    text2 = f"Based on your info: \nYou're a {gender}\nYou're a {zodiac}, and you were born on {datedob} of {modob} in the year {yeardob}."
    text3 = fortune
    text4 = f"\nYou have successfully created an account with this data:\nEmail: {email}\nPassword: {masked_password}"
    if fname != "" and nname != "" and zodiac != "" and password != "" and email != "" and gender != "False":
        resultlbl.config(text=text1 + text2 + "\n\n" + text3 + "\n\n" + text4)
    else:
        resultlbl.config(text="Please fill all the input fields with necessary information.")

# Create the main window
window = tk.Tk()
window.title("Fortune Teller")
window.geometry("400x800")

# Add labels and entry widgets
lbl1 = tk.Label(window, text="Let Me Read Your Fortune!", font=("Times New Roman", 20))
lbl1.pack(pady=10)

lbl2 = tk.Label(window, text="To tell your fortune, fill out the form below!")
lbl2.pack(pady=5)

fnamelbl = tk.Label(window, text="Full Name")
fnamelbl.pack(pady=2)
fnameinput = tk.Entry(window, width=30)
fnameinput.pack(pady=2)

nnamelbl = tk.Label(window, text="Nickname")
nnamelbl.pack(pady=2)
nnameinput = tk.Entry(window, width=30)
nnameinput.pack(pady=2)

zodiaclbl = tk.Label(window, text="Zodiac")
zodiaclbl.pack(pady=5)
zodiacvar = tk.StringVar()
zodiacvar.set("False")

# Zodiac options packed horizontally
zodiac_frame1 = tk.Frame(window)
zodiac_frame1.pack(pady=2)
aquarius = tk.Radiobutton(zodiac_frame1, value="Aquarius", text="Aquarius", variable=zodiacvar)
pisces = tk.Radiobutton(zodiac_frame1, value="Pisces", text="Pisces", variable=zodiacvar)
aries = tk.Radiobutton(zodiac_frame1, value="Aries", text="Aries", variable=zodiacvar)
taurus = tk.Radiobutton(zodiac_frame1, value="Taurus", text="Taurus", variable=zodiacvar)
aquarius.pack(side="left", padx=5)
pisces.pack(side="left", padx=5)
aries.pack(side="left", padx=5)
taurus.pack(side="left", padx=5)

zodiac_frame2 = tk.Frame(window)
zodiac_frame2.pack(pady=2)
gemini = tk.Radiobutton(zodiac_frame2, value="Gemini", text="Gemini", variable=zodiacvar)
cancer = tk.Radiobutton(zodiac_frame2, value="Cancer", text="Cancer", variable=zodiacvar)
leo = tk.Radiobutton(zodiac_frame2, value="Leo", text="Leo", variable=zodiacvar)
virgo = tk.Radiobutton(zodiac_frame2, value="Virgo", text="Virgo", variable=zodiacvar)
gemini.pack(side="left", padx=5)
cancer.pack(side="left", padx=5)
leo.pack(side="left", padx=5)
virgo.pack(side="left", padx=5)

zodiac_frame3 = tk.Frame(window)
zodiac_frame3.pack(pady=2)
libra = tk.Radiobutton(zodiac_frame3, value="Libra", text="Libra", variable=zodiacvar)
scorpius = tk.Radiobutton(zodiac_frame3, value="Scorpius", text="Scorpius", variable=zodiacvar)
sagittarius = tk.Radiobutton(zodiac_frame3, value="Sagittarius", text="Sagittarius", variable=zodiacvar)
capricornus = tk.Radiobutton(zodiac_frame3, value="Capricornus", text="Capricornus", variable=zodiacvar)
libra.pack(side="left", padx=5)
scorpius.pack(side="left", padx=5)
sagittarius.pack(side="left", padx=5)
capricornus.pack(side="left", padx=5)

emaillbl = tk.Label(window, text="Email")
emaillbl.pack(pady=2)
emailinput = tk.Entry(window, width=30)
emailinput.pack(pady=2)

passwordlbl = tk.Label(window, text="Password")
passwordlbl.pack(pady=2)
passwordinput = tk.Entry(window, show="*", width=30)
passwordinput.pack(pady=2)

genderlbl = tk.Label(window, text="Gender")
genderlbl.pack(pady=5)
gendervar = tk.StringVar()
gendervar.set("False")
gender_frame = tk.Frame(window)
gender_frame.pack(pady=2)
gender1 = tk.Radiobutton(gender_frame, value="Male", text="Male", variable=gendervar)
gender2 = tk.Radiobutton(gender_frame, value="Female", text="Female", variable=gendervar)
gender1.pack(side="left", padx=10)
gender2.pack(side="left", padx=10)

doblbl = tk.Label(window, text="Enter your Date of Birth")
doblbl.pack(pady=5)

dob_frame = tk.Frame(window)
dob_frame.pack(pady=2)
datelbl = tk.Label(dob_frame, text="Date")
molbl = tk.Label(dob_frame, text="Month")
yearlbl = tk.Label(dob_frame, text="Year")
datelbl.pack(side="left", padx=5)
molbl.pack(side="left", padx=5)
yearlbl.pack(side="left", padx=5)

dob_input_frame = tk.Frame(window)
dob_input_frame.pack(pady=2)
date = tk.Spinbox(dob_input_frame, from_=1, to=31, width=5, state="readonly")
month = tk.Spinbox(dob_input_frame, from_=1, to=12, width=5, state="readonly")
year = tk.Spinbox(dob_input_frame, from_=1990, to=2024, width=7)
date.pack(side="left", padx=5)
month.pack(side="left", padx=5)
year.pack(side="left", padx=5)

submitbtn = tk.Button(window, text="Submit Data", command=result)
submitbtn.pack(pady=10)

resultlbl = tk.Label(window, text="")
resultlbl.pack(pady=10)

window.mainloop()
