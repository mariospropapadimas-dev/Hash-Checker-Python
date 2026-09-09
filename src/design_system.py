"""The design system for the application."""

from tkinter import font


class DesignSystem:  # pylint: disable=too-few-public-methods
    """The class for the design system."""

    def __init__(self):
        """Initialize the design system."""
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
