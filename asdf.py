
message = "DIEGO cottin!!"
key = 0b100100100001010101010101101100010010001001010100110101010110101101110001011001010101101001010101010001
def encrypt(message, key):
    message_int = 0
    for i in message:
        message_int = x << 8
        message_int += ord(i)
    print(message_int)
    new_message = message_int ^ key
    return new_message



def decrypt2(message, key):
    dec = message ^ key
    new_message = []
    while dec > 0:
        letter = dec % (2**8)
        dec = dec >> 8
        new_message.insert(0, chr(letter))
    new_message = "".join(new_message)
    return new_message

dec = encrypt(message, key)
print(dec)
plaintext = decrypt2(dec, key)
print(plaintext)
print(2**32)