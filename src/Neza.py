import random


def generate_key():
    key = random.randint(1,256)
    return key

def encrypt(message, key):
    message_list = []
    message_int = 0
    for c in message:
        message_list.append(ord(c))
    temp_key = key
    for i in range(len(message_list)):
        message_list[i] = message_list[i] ^ temp_key
        temp_key += ((256 - key) // len(message_list))
    for item in message_list:
        message_int = message_int << 8
        message_int += item
    return message_int

def decrypt(message, key):
    message_list = []
    message_int = 0
    new_message = ""
    while message > 0:
        message_list.insert(0, (message % 2**8))
        message = message >> 8
    temp_key = key
    for i in range(len(message_list)):
        message_list[i] = message_list[i] ^ temp_key
        temp_key += ((256 - key) // len(message_list))
    for item in message_list:
        message_int = message_int << 8
        message_int += item
        new_message += chr(item)
    message_int = message_int << 8
    message_int += key
    return new_message
