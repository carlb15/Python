"""Separate module for Cart and Order."""


class Cart:
    """Shopping cart class."""

    def __init__(self):
        """Initializing a shopping cart."""
        self._contents = dict()

    def __repr__(self):
        """Overriding the repr attribute for printing."""
        return "{0} {1}".format(Cart, self.__dict__)

    def process(self, order):
        """Process the order."""
        if order.add:
            if order.item not in self._contents:
                self._contents[order.item] = 0
            self._contents[order.item] += 1
        elif order.delete:
            if order.item in self._contents:
                self._contents[order.item] -= 1
                if self._contents[order.item] <= 0:
                    del self._contents[order.item]


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
