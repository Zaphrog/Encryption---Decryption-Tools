import Caesar

message = "The arguments you pass are the message and a passcode no longer than twenty five"
enc_mes = Caesar.encrypt(message, 5)
print(enc_mes)
decrypted = Caesar.decrypt(enc_mes, 5)
print (decrypted)

message_2 = "In the auto decrypt function you enter the language instead of the passcode plus the level you want to try"
enc_mes = Caesar.encrypt(message_2, 5)
print(enc_mes)
auto = Caesar.auto_decrypt(enc_mes, "english", 1)
print(auto)