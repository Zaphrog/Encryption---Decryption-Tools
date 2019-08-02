import Neza
example_message = "This just takes the message. You don't even need to input the password to decrypt it!"
key = Neza.generate_key()
print(key)
encrypted_message = Neza.encrypt(example_message, key)
print(encrypted_message)

decrypted_message = Neza.decrypt(encrypted_message, key)
print(decrypted_message)