"""The main hash checker application."""

import tkinter as tk
from tkinter.ttk import Combobox

from src.design_system import DesignSystem
from src.modes.compare_hashes import CompareHashesMode
from src.modes.verify_files import VerifyFilesMode


class HashChecker:
    """The class for the HashChecker application."""

    def __init__(self, root):
        """Initialize the HashChecker application."""
        self.root = root

        self.root.title("Hash Checker")
        self.root.geometry("800x600")

        self.design = DesignSystem()

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
            mode = CompareHashesMode(
                self.content_frame,
                self.design
            )
            mode.draw_ui()

        elif selection == "Verify Files Mode":
            mode = VerifyFilesMode(
                self.content_frame,
                self.design
            )
            mode.draw_ui()

    def draw_ui(self):
        """Draw the UI."""
        self.label_title.pack()

        self.mode_select.current(0)
        self.mode_select.pack(pady=10)

        self.content_frame.pack()

        self.on_selection_change()
