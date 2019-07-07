import Neza_e
import Neza_d
example_message = "First arg is message second arg is passcode"
example_passcode = 12345
encrypted_message = Neza_e.encrypt(example_message, example_passcode)
print(encrypted_message)
decrypted_message = Neza_d.decrypt(encrypted_message, example_passcode)
print(decrypted_message)