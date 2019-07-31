import Neza

example_message = "This just takes the message. You don't even need to input the password to decrypt it!"

encrypted_message = Neza.encrypt(example_message)
print(encrypted_message)

decrypted_message = Neza.decrypt(encrypted_message)
print(decrypted_message)