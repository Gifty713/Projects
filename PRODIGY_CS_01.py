#Caeser Cipher Program

letters ='abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, shift_value ):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter ==' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + shift_value
                if new_index > 25:
                    new_index = new_index - 26
                ciphertext += letters[new_index]

    return ciphertext


def decrypt(ciphertext, shift_value):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter ==' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - shift_value
                if new_index < 0:
                    new_index = new_index + 26
                plaintext += letters[new_index]
    return plaintext



print('Do you want to encrypt or decrypt? ')
words = input('e/d: \n').lower()

if words == 'e':
    print('ENCRYPTION MODE SELECTED')
    plaintext = input("Enter a text you would like to encrypt: ")
    shift_value = int(input("Enter the shift value 2-4: "))
    while 2>shift_value or shift_value>4 :
        print('Invalid! Shift value must be between 2-4.')
        shift_value = int(input("Enter the shift value 2-4: "))
    print(encrypt(plaintext, shift_value))

elif words == 'd':
    print('DECRYPTION MODE SELECTED')
    ciphertext = input("Enter a text you would like to decrypt: ")
    shift_value = int(input("Enter the shift value (2-4): "))
    while 2>shift_value or shift_value>4 :
        print('Invalid! Shift value must be between 2-4.')
        shift_value = int(input("Enter the shift value 2-4: "))
    print(decrypt(ciphertext, shift_value))

else:
    print('Invalid! Select between e/d.')

    