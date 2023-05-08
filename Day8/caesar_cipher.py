from caesar_cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, encrypt):
    res = ""
    # shift forward to encrypt, backward to decrypt
    if not encrypt:
        shift *= -1
    for char in text:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = (pos + shift) % alphabet.__len__()
            res += alphabet[new_pos]
        else:
            res += char
    print(f"Transformed message: {res}")


print(logo)
running = True
while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text_in = input("Type your message:\n").lower()
    shift_in = int(input("Type the shift number:\n"))

    if direction == "encode":
        caesar(text_in, shift_in, True)
    elif direction == "decode":
        caesar(text_in, shift_in, False)
    else:
        print("Invalid input!")

    running = input("Type '1' to restart, '0' to terminate.\n") == '1'
