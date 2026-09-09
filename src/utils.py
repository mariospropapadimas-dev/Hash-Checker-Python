"""Utilities for the application."""

class AppUtils:  # pylint: disable=too-few-public-methods
    """Utility functions for the application."""

    @staticmethod
    def concat_str(str1, str2) -> str:
        """Concatenate two strings with a newline for each one."""
        return str1 + "\n" + str2 + "\n"
