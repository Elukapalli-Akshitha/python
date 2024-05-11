def is_valid_decimal(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False

def is_valid_hexadecimal(input_str):
    valid_chars = set("0123456789ABCDEF")
    input_str = input_str.upper()
    return all(c in valid_chars for c in input_str)

def decimal_to_hexadecimal(decimal):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        decimal = decimal // 16
    return hexadecimal

def hexadecimal_to_decimal(hexadecimal):
    hex_chars = "0123456789ABCDEF"
    decimal = 0
    for digit in hexadecimal:
        decimal = decimal * 16 + hex_chars.index(digit.upper())
    return decimal

def main():
    user_input = input("Enter a decimal number or a hexadecimal number: ")

    if is_valid_decimal(user_input):
        decimal_num = int(user_input)
        hexadecimal = decimal_to_hexadecimal(decimal_num)
        print("Hexadecimal:", hexadecimal)
    elif is_valid_hexadecimal(user_input):
        decimal_num = hexadecimal_to_decimal(user_input)
        print("Decimal:", decimal_num)
    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()