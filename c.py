def encrypt(message, encryption):
    new_message = ""
    for letter in message:
        location = ord(letter)
        location += encryption
        new_message += chr(location)
    return new_message

def decrypt(message, encryption):
    old_message = ""
    for letter in message:
        location = ord(letter)
        location -= encryption
        old_message += chr(location)
    return old_message

enc = encrypt('Testing...123...123#@1!!', 12)
print(enc)
dec = decrypt(enc, 12)
print(dec)