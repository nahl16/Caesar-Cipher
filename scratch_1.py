def caesar_cipher_encrypt(message, shift):
    encrypted_message = []

    for char in message:
        if char.isalpha():  # Check if the character is alphabetic
            # Determine the offset based on the character's case (uppercase or lowercase)
            if char.islower():
                offset = ord('a')
            else:
                offset = ord('A')

            # Apply the Caesar cipher shift
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_message.append(shifted_char)
        else:
            # If the character is not alphabetic, leave it unchanged
            encrypted_message.append(char)

    return ''.join(encrypted_message)

# Get input from the user
plaintext = input("Enter the message to encrypt: ")
shift_value = int(input("Enter the shift value (an integer): "))

# Encrypt the message using the Caesar cipher
encrypted_text = caesar_cipher_encrypt(plaintext, shift_value)

print("Encrypted message:", encrypted_text)
