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
    return message_int, letters

def decrypt(message, key, letters):
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
    decompressed = compress.decompress(new_message, letters)
    message_int = message_int << 8
    message_int += key
    return decompressed


message = "Testing...123"
key = 97
enc, letters = encrypt(message, key)
print(enc)
dec = decrypt(enc, key, letters)
print(dec)