import tkinter as tk
from tkinter import font


class HashChecker:
    def __init__(self, root):

        self.root = root

        self.root.title("Hash Checker")
        self.root.geometry("800x600")

        # Design ahh system
        self.main_title_font = font.Font(
            family="Inter",
            size=30,
            weight="bold"
        )

        self.main_text_font = font.Font(
            family="Inter",
            size=20,
            weight="bold"
        )

        # Labels
        self.label_title = tk.Label(
            text="Hash Checker",
            font=self.main_title_font
        )

        self.entry_prompt_first = tk.Label(
            text="Enter first hash",
            font=self.main_text_font
        )

        self.entry_prompt_second = tk.Label(
            text="Enter second hash",
            font=self.main_text_font
        )

        self.result_label = tk.Label(
            text="",
            font=self.main_text_font
        )

        # Entries for hashes
        self.first_hash = tk.Entry(
            width=60
        )

        self.second_hash = tk.Entry(
            width=60
        )

        # Buttons
        self.check_button = tk.Button(
            text="Check Hashes",
            font=self.main_text_font,
            command=self.check,
            fg="white",
            bg="black"
        )

    def draw_ui(self):
        # Draw UI
        self.label_title.pack()

        self.entry_prompt_first.pack()
        self.first_hash.pack(ipadx=20, ipady=5)

        self.entry_prompt_second.pack()
        self.second_hash.pack(ipadx=20, ipady=5)

        self.check_button.pack(pady=50)

        self.result_label.pack()

    def check(self):
        hash1 = self.first_hash.get()
        hash2 = self.second_hash.get()

        if not hash1 or not hash2:
            self.result_label.config(text="Please enter both hashes")

        elif len(hash1) < 16 or len(hash2) < 16:
            self.result_label.config(
                text="Hashes must be at least 16 characters long"
            )

        elif hash1 == hash2:
            self.result_label.config(
                text="Check complete! Hashes match!"
            )

        else:
            self.result_label.config(
                text="Check complete! Hashes mismatch. "
                     "Files may be corrupted or malicious"
            )


def main():
    root = tk.Tk()
    app = HashChecker(root)
    app.draw_ui()
    root.mainloop()


if __name__ == "__main__":
    main()