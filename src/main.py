"""A simple hash checker application."""

import tkinter as tk

from src.app import HashChecker


def main():
    """Main function to run the hash checker application."""
    root = tk.Tk()
    app = HashChecker(root)
    app.draw_ui()
    root.mainloop()


if __name__ == "__main__":
    main()
