from tkinter import *
from nltk.corpus import words
import random
window = Tk()

#interface ( one entry per letter )
'''
word1 = [Entry(), Entry(), Entry(), Entry(), Entry()]
word2 = [Entry(), Entry(), Entry(), Entry(), Entry()]
word3 = [Entry(), Entry(), Entry(), Entry(), Entry()]
word4 = [Entry(), Entry(), Entry(), Entry(), Entry()]
word5 = [Entry(), Entry(), Entry(), Entry(), Entry()]
word6 = [Entry(), Entry(), Entry(), Entry(), Entry()]
words = [word1, word2, word3, word4, word5, word6]

for word in range(len(words)):
    for i in range(5):
        words[word][i].grid(row = word, column = i)
        print(f"row = {word}", f"column = {i}")
'''
#dictionary shit

row1placed = False
row2placed = False
row3placed= False
row4placed = False
row5placed = False
row6placed = False
row1had=False
row2had = False
row3had = False
row4had = False
row5had = False
row6had = False
winlist = ["witty", "witch"]
winword = random.choice(winlist)
maxwords = 6
def draw():
    labelframe.pack()
    wordframe.pack()
    buttonframe.pack()
    for word in range(len(words)):
        words[word].grid(row = word, column = 0)
    place_button.pack()

    


def checkword(word):
    return True

def color(index, word):
    global winword
    if word[index] == winword[index]:
        return "green"
    elif word[index] in winword:
        return "yellow"
def replace(wordnum):
    global replaced
    global row1placed, row2placed, row3placed, row4placed, row5placed, row6placed
    global row1had, row2had, row3had, row4had, row5had, row6had
    word = words[wordnum].get()
    words[wordnum].destroy()
    words.remove(words[wordnum])
    if not row1placed and not row1had:
        row1placed = True
        print("changed row1placed to true")
    elif not row2placed and not row2had:
        row2placed = True
    elif not row3placed and not row3had:
        row3placed = True
    elif not row4placed and not row4had:
        row4placed = True
    elif not row5placed and not row5had:
        row5placed = True
    elif not row6placed and not row6had:
        row6placed = True
    #placing the labels
    if row1placed and not row1had:
        for i in range(len(row1)):
            row1[i].config(text = word[i], bg = color(i, word))
        for i in range(len(row1)):
            row1[i].grid(row=1, column = i)
        print("placed row 1")
        row1had = True
    if row2placed and not row2had:
        for i in range(len(row2)):
            row2[i].config(text = word[i], bg = color(i, word))
        for i in range(len(row2)):
            row2[i].grid(row=2, column = i)
        print("placed row 2")
        row2had = True
    if row3placed and not row3had:
        for i in range(len(row3)):
            row3[i].config(text = word[i], bg = color(i, word))
        for i in range(len(row3)):
            row3[i].grid(row=3, column = i)
        print("placed row 3")
        row3had = True
    if row4placed and not row4had:
        for i in range(len(row4)):
            row4[i].config(text = word[i], bg = color(i, word))
        for i in range(len(row4)):
            row4[i].grid(row=4, column = i)
        print("placed row 4")
        row4had = True
    if row5placed and not row5had:
        for i in range(len(row5)):
            row5[i].config(text = word[i], bg = color(i, word))
        for i in range(len(row5)):
            row5[i].grid(row=5, column = i)
        print("placed row 5")
        row5had = True
    if row6placed and not row6had:
        for i in range(len(row6)):
            row6[i].config(text = word[i], bg = color(i, word))
        for i in range(len(row6)):
            row6[i].grid(row=6, column = i)
        print("placed row 6")
        row6had = True

def win():
    print("YOU WIN!!!!!!! LESSGOOO :D POG")

def checkinput(e):
    check()

def check():
    toreplace = words[0]
    
    if len(toreplace.get()) == 5 and checkword(toreplace.get()):
        if toreplace.get() == winword:
            win()
        replace(words.index(toreplace))

wordframe = LabelFrame(text = "Words")
buttonframe = LabelFrame(text = "Buttons and shit")
labelframe = LabelFrame(text = "Guessed words")
words = [Entry(wordframe), Entry(wordframe), Entry(wordframe), Entry(wordframe), Entry(wordframe), Entry(wordframe)]
row1 = [Label(labelframe, text = "fuck me"), Label(labelframe, text = "fuck me"), Label(labelframe, text = "fuck me"), Label(labelframe, text = "fuck me"), Label(labelframe, text = "fuck me")]
row2 = [Label(labelframe), Label(labelframe), Label(labelframe), Label(labelframe), Label(labelframe)]
row3 = [Label(labelframe), Label(labelframe), Label(labelframe), Label(labelframe), Label(labelframe)]
row4 = [Label(labelframe), Label(labelframe), Label(labelframe), Label(labelframe), Label(labelframe)]
row5 = [Label(labelframe), Label(labelframe), Label(labelframe), Label(labelframe), Label(labelframe)]
row6 = [Label(labelframe), Label(labelframe), Label(labelframe), Label(labelframe), Label(labelframe)]

checked = []
place_button = Button(buttonframe, text = "Check", command = check)
    

#placing the labels and shit



#drawing the starting stuffs
draw()
window.bind('<Return>', checkinput)
window.mainloop()
