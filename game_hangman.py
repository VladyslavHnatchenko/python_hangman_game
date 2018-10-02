# import all necessary libraries
from tkinter import *
from tkinter import ttk
import random


# create start page with instruction
def but():
    y = 0
    while y < 600:
        x = 0
        while x < 600:
            canvas.create_rectangle(x, y, x+33, y+27, fill="white", outline="blue")
            x = x+33
        y = y+27


faq = '''Hello player! Are you ready?
HOW TO PLAY:
Choose one person to be the executioner. 
That person will think of a word or short phrase 
an mark out blanks (short lines) for each letter 
of each word. Separate words with either a slash,
a fairly wide gap, or place words on separate lines. 
Then another player will guess a letter. If that 
letter is in the word(s) then write the letter in 
everywhere it would appear, an cross out that letter
in the alphabet. If the letter isn't in the word then 
add a body part to the gallows (head, body, left arm,
right arm, left leg, right leg). The player will continue
guessing letters until they can either solve the word 
(or phrase) or all six body parts are on the gallows.
TO WIN:
The executioner wins if the full body is hanging from 
the gallows. The guesser(s) wins if they guess the word 
before the person is hung.'''

# draw a window
root = Tk()
root.title("Gallows")
canvas = Canvas(root, width=600, height=600)
canvas.pack()
canvas.create_text(310, 240, text=faq, fill="blue", font=("Helvetica", "14"))
words = ["business", "champion", "ceremony", "interval", "children", "reporter", "victoria",
         "tomorrow", "training", "workshop", "terminal", "swimming", "survival", "variable",
         "software", "solution", "sequence", "remember", "recovery", "producer", "language"]

btn01 = Button(root, text="Start!", width=10, height=1, command=lambda: arr())
btn01.place(x=258, y=542)
btn01["bg"] = "grey"


# create all functions
def arr():
    but()
    word = random.choice(words)
    wo = word[1:-1]
    wor = []
    for i in wo:
        wor.append(i)
        a0 = canvas.create_text(282, 40, text=word[0], fill="blue", font=("Helvetica", "18"))
        a1 = canvas.create_text(315, 40, text="_", fill="blue", font=("Helvetica", "18"))
        a2 = canvas.create_text(347, 40, text="_", fill="blue", font=("Helvetica", "18"))
        a3 = canvas.create_text(380, 40, text="_", fill="blue", font=("Helvetica", "18"))
        a4 = canvas.create_text(412, 40, text="_", fill="blue", font=("Helvetica", "18"))
        a5 = canvas.create_text(444, 40, text="_", fill="blue", font=("Helvetica", "18"))
        a6 = canvas.create_text(477, 40, text="_", fill="blue", font=("Helvetica", "18"))
        a7 = canvas.create_text(510, 40, text=word[-1], fill="blue", font=("Helvetica", "18"))

    list1 = [1, 2, 3, 4, 5, 6]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    er = []
    win = []

    def a(v):
        ind_alf = alphabet.index(v)
        key = alphabet[ind_alf]

        if v in wor:
            ind = wor.index(v)
            b2 = list1[ind]
            wor[ind] = '1'

            def kord():
                if b2 == 1:
                    x1, y1 = 315, 40
                if b2 == 2:
                    x1, y1 = 347, 40
                if b2 == 3:
                    x1, y1 = 380, 40
                if b2 == 4:
                    x1, y1 = 412, 40
                if b2 == 5:
                    x1, y1 = 444, 40
                if b2 == 6:
                    x1, y1 = 477, 40
                return x1, y1

            x1, y1 = kord()
            win.append(v)
            a2 = canvas.create_text(x1, y1, text=wo[ind], fill="blue", font=("Helvetica", "18"))
            btn[key]["bg"] = "green"

            if not v in wor:
                btn[key]["state"] = "disabled"
            if v in wor:
                win.append(v)
                ind2 = wor.index(v)
                b2 = list1[ind2]
                x1, y1 = kord()
                canvas.create_text(x1, y1, text=wo[ind2], fill="blue", font=("Helvetica", "18"))
            if len(win) == 6:
                canvas.create_text(150, 150, text="You won!", fill="grey", font=("Helvetica", "26"))
                for i in alphabet:
                    btn[i]["state"] = "disabled"
        else:
            er.append(v)
            btn[key]["bg"] = "red"
            btn[key]["state"] = "disabled"

            if len(er) == 1:
                head()
            elif len(er) == 2:
                body()
            elif len(er) == 3:
                rightHand()
            elif len(er) == 4:
                leftHand()
            elif len(er) == 5:
                leftLeg()
            elif len(er) == 6:
                rightLeg()
                end()
            root.update()

    btn = {}

    def gen(u, x, y):

        btn[u] = Button(root, text=u, width=3, height=1, command=lambda: a(u))
        btn[u].place(x=str(x), y=str(y))
    x = 265
    y = 110
    for i in alphabet[0:8]:
        gen(i, x , y)
        x = x + 33
    x = 265
    y = 137
    for i in alphabet[8:16]:
        gen(i, x, y)
        x = x + 33
    x = 265
    y = 164
    for i in alphabet[16:24]:
        gen(i, x, y)
        x = x + 33
    x = 265
    y = 191
    for i in alphabet[24:33]:
        gen(i, x, y)
        x = x + 33

    def head():
        canvas.create_oval(79, 59, 120, 80, width=4, fill='white')
        root.update()

    def body():
        canvas.create_line(100, 80, 100, 200, width=4)
        root.update()

    def rightHand():
        canvas.create_line(100, 80, 145, 100, width=4)
        root.update()

    def leftHand():
        canvas.create_line(100, 80, 45, 100, width=4)
        root.update()

    def leftLeg():
        canvas.create_line(100, 200, 45, 300, width=4)
        root.update()

    def rightLeg():
        canvas.create_line(100, 200, 145, 300, width=4)
        root.update()

    def end():
        canvas.create_text(150, 150, text="You lose!", fill="red", font=("Helvetica", "24"))
        for i in alphabet:
            btn[i]["state"] = "disabled"


root.mainloop()
