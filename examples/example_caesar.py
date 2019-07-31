import Caesar

message = "The arguments you pass are the message and a passcode no longer than twenty five"
enc_mes = Caesar.encrypt(message, 5)
print(enc_mes)
decrypted = Caesar.decrypt(enc_mes, 5)
print (decrypted)

message_2 = "The longer the message the easier it is for the program to decrypt it without knowing the passcode"
enc_mes = Caesar.encrypt(message_2, 5)
print(enc_mes)
auto = Caesar.auto_decrypt(enc_mes, "english", 1)
print(auto)

message_3 = "If you want to encrypt special characters, it is better to use encrypt_ascii. That function can take in any ascii character! The disadvantage is that the auto_decrypt function does not work on this one."
encrypted = Caesar.encrypt_ascii(message_3, 24)
print(encrypted)
decrypted_ascii = Caesar.decrypt_ascii(encrypted, 24)
print(decrypted_ascii)