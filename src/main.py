from tkinter import *
from tkinter import font


# Functions

def check():
    hash1 = firstHash.get()
    hash2 = secondHash.get()

    if hash1 is None or hash2 is None:
        resultLabel.config(text="Empty Hash")
    elif hash1 == hash2:
        resultLabel.config(text="Check complete! Hashes match!")
    else:
        resultLabel.config(text="Check complete! Hashes mismatch. Files may be corrupted or malicious")

    # initialization


window = Tk()

window.title("Hash Checker")

window.geometry("800x600")

# Design ahh system
mainTitleFont = font.Font(
    family="Inter",
    size=25,
    weight="bold"
)

mainTextFont = font.Font(
    family="Inter",
    size=10,
    weight="bold"
)

# Labels

labelTitle = Label(
    text="Hash Checker",
    font=mainTitleFont
)

entryPromptFirst = Label(
    text="Enter first hash",
    font=mainTextFont
)

entryPromptSecond = Label(
    text="Enter second hash",
    font=mainTextFont
)

resultLabel = Label(
    text="",
    font=mainTextFont
)

# entries for hashes

firstHash = Entry()
secondHash = Entry()

# Buttons

checkButton = Button(
    text="Check Hashes",
    font=mainTextFont,
    command=check,
    fg="white",
    bg="black"
)

# Draw UI

labelTitle.pack()

entryPromptFirst.pack()
firstHash.pack()
entryPromptSecond.pack()
secondHash.pack()

checkButton.place(x=350, y=150)

resultLabel.pack()

# Dont code below this line
window.mainloop()