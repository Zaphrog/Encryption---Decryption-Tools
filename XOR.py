
def encrypt(message, key):
    message_int = 0
    for i in message:
        message_int = message_int << 8
        message_int += ord(i)
    new_message = message_int ^ key
    return new_message

def decrypt(message, key):
    dec = message ^ key
    old_message = []
    while dec > 0:
        letter = dec % (2**8)
        dec = dec >> 8
        old_message.insert(0, chr(letter))
    old_message = "".join(old_message)
    return old_message
