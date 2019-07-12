# Caesar_Python

Caesar is a very simple and popular encryption method:
- First each letter is represented by a number.
- Then you pick a number and add it to the number equivalent of each letter.

For example: `HELLO (8, 5, 12, 12, 15)` encrypted with `5` would be `MJQQT (13, 9, 18, 18, 20)`.

The global variable `alphabet` is a list with the most used letters in the english, spanish and german alphabets. You choose the language.
```py
alphabet = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X", "Y", "Z"]
```

If the number after the encryption exceeds the length of the given alphabet (26), you just do n - 26.

In the first code you can encrypt and decrypt the message, but the encryption already knows the encryption value.
So i added a second code with which you can decrypt the message without knowing the encryption value.

In a longer message, it is almost 100% sure that the most used character would be ' ' (spacebar), so it will assume that the character most used in the encrypted message is spacebar and will calculate the encryption value.

There are other settings, so you can encrypt shorter messages after a few attempts. It changes settings just by pressing "ENCRYPT" again.

#NEZA

Neza is basically an XOR cipher with a password that changes with every block.
The first thing the program does when encrypting a message is dividing it into chunks by appending the ASCII code of
each character to a list. It then randomly generates an 8 bit passcode and calculates the rate of change. That is done by
 `temp_key += ((256 - key) // len(message_list))`. It generates an equal change for each step. At the last step it must be as close to 256 as possible.
 For each letter in the list of the message it runs an XOR calculation with the modified key. At the end it reassembles a new message using the
 ASCII code of the new values. The last step is appending the ASCII code of the key to the new_message, which allows decryption.

 To decrypt the message, the program removes the last letter (the key) from the message and runs the same calculation to calculate the rate of change.
 Then it just reverts the XOR for every letter and appends the correct letters to a message.

 Its main weakness is that the length of the message is evident.