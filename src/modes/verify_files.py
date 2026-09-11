"""The VerifyFilesMode mode for the application."""

import tkinter as tk
from tkinter import filedialog


class VerifyFilesMode:
    # pylint: disable=too-few-public-methods
    """The class for the VerifyFilesMode mode."""

    def __init__(self, parent, design):
        """Initialize the VerifyFilesMode mode."""
        self.file_path = None
        self.parent = parent
        self.design = design

        self.select_file = tk.Button(
            self.parent,
            text="Select File",
            font=self.design.main_text_font,
            command=self.select_file
        )

        self.selected_file_path = tk.Label(
            self.parent,
            text= f"Select File: {self.file_path}",
            font=self.design.main_text_font
        )


    def draw_ui(self):
        """Draw the UI."""
        self.select_file.pack(ipady=10)
        self.selected_file_path.pack(ipady=1)

    def select_file(self):
        """Select the file to verify and print path"""
        self.file_path = filedialog.askopenfilename()
        print(self.file_path)
