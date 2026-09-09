"""A simple hash checker application."""

import tkinter as tk
from tkinter import font
from tkinter.ttk import Combobox


class AppUtils:
    """Utility functions for the application."""

    @staticmethod
    def concat_str(str1, str2) -> str:
        """Concatenate two strings with a newline for each one."""
        return str1 + "\n" + str2 + "\n"

class DesignSystem:
    """The class for the design system"""
    def __init__(self):
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

class HashChecker:
    """The class for the HashChecker application."""
    def __init__(self, root):
        """Initialize the HashChecker application."""
        self.root = root

        self.root.title("Hash Checker")
        self.root.geometry("800x600")

        self.design = DesignSystem()

        # Labels
        self.label_title = tk.Label(
            text="Hash Checker",
            font=self.design.main_title_font
        )

        self.mode_select = Combobox(
            self.root,
            values=["Compare Hashes Mode", "Verify Files Mode"],
            state="readonly",
            width=25
        )

        self.mode_select.bind(
            "<<ComboboxSelected>>",
            self.on_selection_change
        )

        self.content_frame = tk.Frame(self.root)


    def on_selection_change(self, _event=None):
        """Change the hash checker mode."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        selection = self.mode_select.get()

        if selection == "Compare Hashes Mode":
            mode = CompareHashesMode(self.content_frame, self.design)
            mode.draw_ui()

        elif selection == "Verify Files Mode":
            mode = VerifyFilesMode(self.content_frame, self.design)
            mode.draw_ui()


    def draw_ui(self):
        """Draw the UI"""
        self.label_title.pack()

        self.mode_select.current(0)
        self.mode_select.pack(pady=10)

        self.content_frame.pack()

        self.on_selection_change()



class CompareHashesMode:
    """The class for the compare hashes mode"""
    def __init__(self, parent, design):
        """Initialize the HashChecker compare mode."""

        self.design = design
        self.parent = parent

        self.entry_prompt_first = tk.Label(
            self.parent,
            text="Enter first hash",
            font=self.design.main_text_font
        )

        self.entry_prompt_second = tk.Label(
            self.parent,
            text="Enter second hash",
            font=self.design.main_text_font
        )

        self.result_label = tk.Label(
            self.parent,
            text="",
            font=self.design.main_text_font
        )

        # Entries for hashes
        self.first_hash = tk.Entry(
            self.parent,
            width=60
        )

        self.second_hash = tk.Entry(
            self.parent,
            width=60
        )

        # Buttons
        self.check_button = tk.Button(
            self.parent,
            text="Check Hashes",
            font=self.design.main_text_font,
            command=self.check,
            fg="white",
            bg="black"
        )

    def draw_ui(self):
        """Draw the UI"""
        self.entry_prompt_first.pack()
        self.first_hash.pack(ipadx=20, ipady=5)

        self.entry_prompt_second.pack()
        self.second_hash.pack(ipadx=20, ipady=5)

        self.check_button.pack(pady=50)

        self.result_label.pack()

    def check(self):
        """Check if the two hashes match."""

        # Getting the hashes from the entries and using .strip() to remove any whitespaces
        hash1 = self.first_hash.get().strip()
        hash2 = self.second_hash.get().strip()

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
                text=AppUtils.concat_str("Check complete! Hashes mismatch. \n ",
                                     "Files may be corrupted or malicious")
            )

class VerifyFilesMode:
    """The class for the VerifyFilesMode mode"""
    def __init__(self, parent, design):
        """Initialize the VerifyFilesMode mode."""

        self.parent = parent
        self.design = design

        self.under_construction = tk.Label(
            self.parent,
            text="Under Construction",
            font=self.design.main_text_font
        )

    def draw_ui(self):
        """Draw the UI"""
        self.under_construction.pack()


def main():
    """Main function to run the hash checker application."""
    root = tk.Tk()
    app = HashChecker(root)
    app.draw_ui()
    root.mainloop()


if __name__ == "__main__":
    main()
