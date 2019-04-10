import tkinter
import collections
import sys
import os

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
        
global attempts
attempts = []

def reset():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def end():
    decrypt.destroy()

def add_attempt():
    attempts.append("1")
        
def turn():
    message = m.get()
    message = message.upper()
    print (message)
    language = l.get()
    language = language.upper()
    print (language)
    most_used = str(languages[language]["most_used"])
    print (most_used)
    repeated = collections.defaultdict(int)
    for c in message:
        repeated[c] += 1
    print (repeated)
    used_letter = max(repeated.keys(), key=(lambda k: repeated[k]))
    print (used_letter)
    most_location =  int(alphabet.index(most_used[len(attempts)]))
    print (most_location)
    encryption = - most_location + int(alphabet.index(used_letter))
    print (encryption)
    old_message = ""
    for c in message:
        location = int(alphabet.index(c))
        old_location = location - encryption
        if old_location < 0:
            old_location = old_location +26
        elif old_location > 26:
            old_location = old_location - 26
        old_message = old_message + alphabet[old_location]
        print (old_message)
    pom ["text"]= "Decrypted Message: " + (old_message)
    add_attempt()
    print (attempts)
    
decrypt = tkinter.Tk()
decmes = tkinter.Label(decrypt, text = "Write encrypted message: ")
decmes.pack()
global m
m = tkinter.Entry(decrypt)
m.pack()
lan = tkinter.Label(decrypt, text = "Write the language of the message: ")
lan.pack()
global l
l = tkinter.Entry(decrypt)
l.pack()
decryptmes = tkinter.Button(decrypt, text = "Decrypt Message", command = turn)
decryptmes.pack()
pom = tkinter.Label(decrypt, text = "Decrypted Message: ")
pom.pack()
reset = tkinter.Button(decrypt, text= "Reset", command= reset)
reset.pack(side = "left")
end = tkinter.Button(decrypt, text = "End", command= end)
end.pack(side= "right")
decrypt.mainloop()

