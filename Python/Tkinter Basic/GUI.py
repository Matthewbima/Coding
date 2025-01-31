import tkinter as tk
import random


def changetext():
    global i
    if i % 2 == 1:
        btn2.configure(text="the text is changing !")
        i += 1
    else:
        btn2.configure(text="Click Me NOW!")
        i += 1

def clrlabel():
    global i
    if i % 2 == 1:
        lbl5.configure(fg="red", bg="black")
        i += 1
    else:
        lbl5.configure(fg="#000000", bg="#f0f0f0")
        i += 1

def clrbtn():
    global i
    if i % 2 == 1:
        btn4.configure(fg="blue", bg="orange")
        i += 1
    else:
        btn4.configure(fg="#000000", bg="#f0f0f0")
        i += 1

def countclick():
    global totalclick
    totalclick = totalclick + 1
    newstr = "You have click the button " + str(totalclick) + " time(s)"
    lbl7.configure(text=newstr)

def quizGenerate():
    global num1, num2, symbol, shuffled_items, items, answerTemp0
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    symbol = random.choice(["+","-","*","/"])
    if symbol == "+":
        answerTemp0 = num1 + num2
    elif symbol == "-":
        answerTemp0 = num1 - num2
    elif symbol == "/":
        answerTemp0 = num1 / num2
    elif symbol == "*":
        answerTemp0 = num1 * num2
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    items = [a, b, answerTemp0]
    shuffled_items = random.sample(items, len(items))
    questions.configure(text="What is : " + str(num1) + symbol + str(num2) +" ?")
    answer1.configure(text=shuffled_items[0])
    answer2.configure(text=shuffled_items[1])
    answer3.configure(text=shuffled_items[2])

def checkAnswer(button):
    global answerTemp0, score

    if button.cget("text") == answerTemp0:
        score += 1  # Increment score for correct answer
        scorelabel.configure(text="You have " + str(score) + " correct answer(s)", bg="green", fg="white")
    else:
        scorelabel.configure(bg="red",fg="white")

    quizGenerate()



totalclick  = 0
i=1

num1 = 0
num2 = 0
symbol = random.choice(["+","-","*","/"])
score = 0
items = []
shuffled_items = random.sample(items, len(items))



root = tk.Tk()
root.title("My Own GUI")
root.geometry("1080x800")
img = tk.PhotoImage(file="image.png")
img = img.subsample(max(1, img.width() // 150), max(1, img.height() // 150))

lbl = tk.Label(root, image=img)
lbl2 = tk.Label(root, text="This is a label, a label shows you a text")
lbl3 = tk.Label(root, text="There is also a button, which we can click to make it do something")
btn = tk.Button(root, text="I'm a button, try to click me !")
lbl4 = tk.Label(root, text="Now let's try this one, which will do something !")
btn2 = tk.Button(root, text="Click Me NOW!", command=changetext)
lbl5 = tk.Label(root, text="we can also change the color")
btn3 = tk.Button(root, text="Click me to change the label's color", command=clrlabel)
btn4 = tk.Button(root, text="Click me to change the color of the button", command=clrbtn)
lbl6= tk.Label(root, text="we can also do something like a counting function")
btn5= tk.Button(root, text="Click to increase your counter", command = countclick)
lbl7= tk.Label(root, text="")
lbl8=tk.Label(root, text="We can also make a simple quiz like :")
questions=tk.Label(root, text="")
answer1=tk.Button(root, text="", command = lambda: checkAnswer(answer1))
answer2=tk.Button(root, text="", command = lambda: checkAnswer(answer2))
answer3=tk.Button(root, text="", command = lambda: checkAnswer(answer3))
scorelabel=tk.Label(root,text="")

quizGenerate()

lbl.pack(padx=5, pady=5)
lbl2.pack(padx=5, pady=5)
lbl3.pack(padx=5, pady=5)
btn.pack(padx=5, pady=5)
lbl4.pack(padx=5, pady=5)
btn2.pack(padx=5, pady=5)
lbl5.pack(padx=5, pady=5)
btn3.pack(padx=5, pady=5)
btn4.pack(padx=5, pady=5)
lbl6.pack(padx=5, pady=5)
btn5.pack(padx=5, pady=5)
lbl7.pack(padx=5, pady=5)
lbl8.pack(padx=5, pady=5)
questions.pack(padx=5, pady=5)
answer1.pack(padx=5, pady=5)
answer2.pack(padx=5, pady=5)
answer3.pack(padx=5, pady=5)
scorelabel.pack(padx=5, pady=5)

root.mainloop()