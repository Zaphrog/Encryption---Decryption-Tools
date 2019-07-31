import collections
global alphabet
alphabet = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X", "Y", "Z"]

global languages
languages = {
    "ENGLISH":{
        "most_used":" ETAOINSRHLDCUMFP"
        },
    "SPANISH":{
        "most_used":"EAOSRNIDLCTUMPB"
        },
    "GERMAN":{
        "most_used": "ENIRSTAHDULCGMO"
        }
    }

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
    old_message_decrypt = ""
    for letter in new_message:
        location = int(alphabet.index(letter))
        old_location = location - encryption
        if old_location < 0:
            old_location = old_location + 26
        old_message_decrypt = old_message_decrypt + alphabet[old_location]
    return old_message_decrypt

def auto_decrypt(message, language, iterations):
    message = message.upper()
    language = language.upper()
    most_used = str(languages[language]["most_used"])
    repeated = collections.defaultdict(int)
    for c in message:
        repeated[c] += 1
    used_letter = max(repeated.keys(), key=(lambda k: repeated[k]))
    most_location = int(alphabet.index(most_used[iterations-1]))
    encryption = - most_location + int(alphabet.index(used_letter))
    old_message_auto = ""
    for c in message:
        location = int(alphabet.index(c))
        old_location = location - encryption
        if old_location < 0:
            old_location = old_location +26
        elif old_location > 26:
            old_location = old_location - 26
        old_message_auto = old_message_auto + alphabet[old_location]
    return old_message_auto

def encrypt_ascii(message, encryption):
    new_message = ""
    for letter in message:
        location = ord(letter)
        location += encryption
        new_message += chr(location)
    return new_message

def decrypt_ascii(message, encryption):
    old_message = ""
    for letter in message:
        location = ord(letter)
        location -= encryption
        old_message += chr(location)
    return old_message
