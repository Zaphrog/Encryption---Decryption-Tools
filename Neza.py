import random

def encrypt(message):
    message_list = []
    message_int = 0
    new_message = ""
    for c in message:
        message_list.append(ord(c))
    key = random.randint(1,256)
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
    new_message += chr(key)
    return new_message

def decrypt(message):
    message_list = []
    message_int = 0
    new_message = ""
    for c in message:
        message_list.append(ord(c))
    key = message_list[-1]
    message_list.pop()
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

