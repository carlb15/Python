"""Part 3: Shopping functions."""


def get_order():
    """Retrieve the order."""
    print("[command] [item] (command is a to add, d to delete, q to quit).")
    line = input()
    command = line[:1]
    item = line[2:]

    return command, item


def add_to_cart(item, cart):
    """Add item to the cart."""
    if item not in cart:
        cart[item] = 0
    cart[item] += 1


def remove_from_cart(item, cart):
    """Delete an item from the cart."""
    if item in cart and cart[item] > 1:
        cart[item] -= 1
    elif item in cart and cart[item] == 1:
        del cart[item]


def process_order(order, cart):
    """Processing the order."""
    command, item = order

    if command == "a":
        add_to_cart(item, cart)
    elif command == "d" and item in cart:
        remove_from_cart(item, cart)
    elif command == "q":
        return False

    return True


def go_shopping():
    """Go shopping."""
    cart = {}

    while True:
        order = get_order()
        if not process_order(order, cart):
            break

    print(cart)
    print("Finished")


go_shopping()
