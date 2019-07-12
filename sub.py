import random
import SHA256
import sys

def enter(correct_passcode):
    passcode = input("Enter the passcode: ")
    p = SHA256.pad_message(passcode)
    s = SHA256.SHA256(p)
    if s == correct_passcode:
        print("Access granted")
        return
    else:
        print("Access denied")
        sys.exit()

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

def run():
    passcode = "Arepa123"
    p1 = SHA256.pad_message(passcode)
    hp = SHA256.SHA256(p1)
    enter(hp)
    user = input("Enter 'E' if you would like to encrypt. Enter 'D' if you would like to decrypt: ")
    if user == "E":
        message = input("Enter your message: ")
        enc = encrypt(message)
        print(enc)
    elif user == "D":
        message = input("Enter the encrypted message: ")
        dec = decrypt(message)
        print(dec)

run()