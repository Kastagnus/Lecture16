
def ask_input():
    digit = input("1 - Check Balance\n2 - Make a Deposit\n3 - Withdraw\nChoose the operation (1,2 or 3): ")
    if digit.isdigit() and int(digit) in [1, 2, 3]:
        return int(digit)
    else:
        return None


def display_screen(digit):
    ...