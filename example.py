import Neza
import Neza
example_message = "First arg is message second arg is passcode"
example_passcode = 12345
encrypted_message = Neza.encrypt(example_message, example_passcode)
print(encrypted_message)
decrypted_message = Neza.decrypt(encrypted_message, example_passcode)
print(decrypted_message)