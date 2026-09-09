"""The VerifyFilesMode mode for the application."""


import tkinter as tk

class VerifyFilesMode:  # pylint: disable=too-few-public-methods
    """The class for the VerifyFilesMode mode."""

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
        """Draw the UI."""
        self.under_construction.pack()
