"""Separate module for Order."""


class Order:
    """Order class."""

    def __init__(self):
        """Initializing the order."""
        self.quit = False
        self.add = False
        self.delete = False
        self.item = None

    def get_input(self):
        """Retrieve the order."""
        print("[command] [item] (command: a to add, d to delete, q to quit).")
        line = input()
        command = line[:1]
        self.item = line[2:]

        if command == 'a':
            self.add = True
        elif command == 'q':
            self.quit = True
        elif command == 'd':
            self.delete = True
