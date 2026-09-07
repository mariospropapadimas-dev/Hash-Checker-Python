from tkinter import *
from tkinter import font


# Functions

def check():
    hash1 = firstHash.get()
    hash2 = secondHash.get()

    if hash1 == "" or hash2 == "":
        resultLabel.config(text="Please enter both hashes")
    elif len(hash1) < 16 or len(hash2) < 16:
        resultLabel.config(text="Hashes must be at least 16 characters long")
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
    size=30,
    weight="bold"
)

mainTextFont = font.Font(
    family="Inter",
    size=20,
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

firstHash = Entry(
    width=60
)
secondHash = Entry(
    width=60
)

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
firstHash.pack(ipadx=20, ipady=5)
entryPromptSecond.pack()
secondHash.pack(ipadx=20, ipady=5)

checkButton.pack(pady=50)

resultLabel.pack()

# Dont code below this line
window.mainloop()