from src import Caesar
from src.utils import print_table

# SPECIAL CHARACTERS
message = "The arguments you pass are the message and a passcode no longer than twenty five"
enc_mes = Caesar.encrypt(message, 5)
decrypted = Caesar.decrypt(enc_mes, 5)

print_table([['decrypted message', decrypted],
             ['encrypted message', enc_mes]])

# Guessing decryption
message_2 = "The longer the message the easier it is for the program to decrypt it without knowing the passcode"
enc_mes = Caesar.encrypt(message_2, 5)
auto = Caesar.auto_decrypt(enc_mes, "english", 1)

print_table([['decrypted message', auto],
             ['encrypted message', enc_mes]])

# SPECIAL CHARACTERS
message_3 = "Encrypt special characters with encrypt_ascii. The disadvantage is that the auto_decrypt function does not work on this one."
encrypted = Caesar.encrypt_ascii(message_3, 24)
decrypted_ascii = Caesar.decrypt_ascii(encrypted, 24)

print_table([['decrypted message', decrypted_ascii],
             ['encrypted message', encrypted]])