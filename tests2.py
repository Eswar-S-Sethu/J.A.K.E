import time
from itertools import product


def generate_pin_combinations(pin_length):
    """Generate all possible PIN combinations of the given length."""
    for pin_tuple in product("0123456789", repeat=pin_length):
        # Join the tuple to form the PIN string
        yield ''.join(pin_tuple)  # Use yield to create a generator


def check_pin(pin, target_pin):
    """Check if the generated PIN matches the target PIN."""
    return pin == target_pin


def brute_force_pin(target_pin, pin_length):
    """Brute-force the PIN by generating combinations and checking them."""
    for formatted_pin in generate_pin_combinations(pin_length):
        print(f'Trying PIN: {formatted_pin}')


        if check_pin(formatted_pin, target_pin):
            print(f'Success! The PIN is: {formatted_pin}')
            return formatted_pin

    print('Failed to find the PIN within the specified length.')
    return None


# Example usage
target_pin = '13062002'  # Set your target PIN code here
pin_length = len(target_pin)  # Set the length of the PIN code
brute_force_pin(target_pin, pin_length)
