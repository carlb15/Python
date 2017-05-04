"""Demonstrate raiding a refrigerator."""
from contextlib import closing


class RefrigeratorRaider:
    """Raid a refrigerator."""

    def open(self):
        """Open refrigerator door."""
        print("Open fridge door.")

    def take(self, food):
        """Take food from the refrigerator."""
        print("Finding {}...".format(food))
        if food == 'deep fried pizza':
            raise RuntimeError("Health warning!")
        print("Taking {}".format(food))

    def close(self):
        """Close the refrigerator door."""
        print("Close fridge door.")


def raid(food):
    "Raid the refrigerator."
    # Closing ensures the close method is always called before exiting.
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)
