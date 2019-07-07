
global alphabet
alphabet = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X", "Y", "Z"]


def encrypt(message, encryption):
    message = message.upper()
    new_message = ""
    for letter in message:
        location = int(alphabet.index(letter))
        new_location = location + encryption
        if new_location >= 27:
            new_location = new_location - 26
        new_message = new_message + alphabet[new_location]
    return new_message


def decrypt(new_message, encryption):
    new_message = new_message.upper()
    old_message = ""
    for letter in new_message:
        location = int(alphabet.index(letter))
        old_location = location - encryption
        if old_location < 0:
            old_location = old_location + 26
        old_message = old_message + alphabet[old_location]
    return old_message

enc = encrypt("Hello", 5)
print(enc)
dec = decrypt(enc, 5)
print (dec)
