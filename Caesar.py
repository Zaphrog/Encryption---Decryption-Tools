import tkinter
import os
import sys


global alphabet
alphabet = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X", "Y", "Z"]

def reset():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def end():
    mainCaesar.destroy()

def turn():
    message = m.get()
    message = message.upper()
    encryption = int(e.get())
    new_message = ""
    for letter in message:
        location = int(alphabet.index(letter))
        new_location = location + encryption
        if new_location >= 27:
            new_location = new_location - 26
        new_message = new_message + alphabet[new_location]
        print (new_message)
    pnm["text"] = "Encrypted message: " + (new_message)  
    newmessage = nm.get()
    newmessage = newmessage.upper()
    old_message = ""
    for letter in newmessage:
        location = int(alphabet.index(letter))
        old_location = location - encryption
        if old_location < 0:
            old_location = old_location + 26
        old_message = old_message + alphabet[old_location]
    pom["text"]= old_message
    

mainCaesar = tkinter.Tk()
encmes = tkinter.Label(mainCaesar, text = "Write Message")
encmes.pack()
global m
m = tkinter.Entry(mainCaesar)
m.pack()
enc = tkinter.Label(mainCaesar, text = "Encryption value")
enc.pack()
global e
e = tkinter.Entry(mainCaesar)
e.pack()
encryptmes = tkinter.Button(mainCaesar, text = "Encrypt Message", command = turn)
encryptmes.pack()
pnm = tkinter.Label(mainCaesar, text = "Encrypted Message: ")
pnm.pack()
decmes = tkinter.Label(mainCaesar, text = "Write Message to decrypt")
decmes.pack()
global nm
nm = tkinter.Entry(mainCaesar)
nm.pack()
decryptmes = tkinter.Button(mainCaesar, text = "Decrypt Message", command = turn)
decryptmes.pack()
pom = tkinter.Label(mainCaesar, text = "Decrypted message: ")
pom.pack()
reset= tkinter.Button(mainCaesar, text = "Reset", command= reset)
reset.pack(side = "left")
end = tkinter.Button(mainCaesar, text = "End", command= end)
end.pack(side= "right")
mainCaesar.mainloop()

