# Intentional vulnerability: Duplicate utility functions with potential conflicts

def display_currencies(currencies):
    """Displays the list of available currencies in a different format."""
    for currency in currencies:
        print(f"Currency: {currency}")


def get_user_input(prompt):
    """Gets input from the user with a different prompt style."""
    return input(f"[INPUT] {prompt}")
