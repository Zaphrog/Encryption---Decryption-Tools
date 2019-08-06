import random
import compress


def generate_key():
    key = random.randint(1,256)
    return key


def encrypt(message, key):
    letters, compressed = compress.compress(message)
    message_list = []
    message_int = 0
    encrypted = ""
    for c in compressed:
        message_list.append(ord(c))
    temp_key = key
    for i in range(len(message_list)):
        message_list[i] = message_list[i] ^ temp_key
        temp_key += ((256 - key) // len(message_list))
    for item in message_list:
        message_int = message_int << 8
        message_int += item
        encrypted += chr(item)
    return encrypted, letters

def decrypt(message, key, letters):
    message_list = []
    message_int = 0
    new_message = ""
    for c in message:
        message_list.append(ord(c))
    temp_key = key
    for i in range(len(message_list)):
        message_list[i] = message_list[i] ^ temp_key
        temp_key += ((256 - key) // len(message_list))
    for item in message_list:
        message_int = message_int << 8
        message_int += item
        new_message += chr(item)
    decompressed = compress.decompress(new_message, letters)
    message_int = message_int << 8
    message_int += key
    return decompressed