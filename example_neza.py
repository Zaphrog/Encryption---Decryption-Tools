from src import Neza
from src.utils import print_table

example_message = "This just takes the message. You don't even need to input the password to decrypt it!"
key = Neza.generate_key()
encrypted_message, letters = Neza.encrypt(example_message, key)
decrypted_message = Neza.decrypt(encrypted_message, key, letters)

print_table([['key', str(key)],
             ['decrypted message', str(decrypted_message)],
             ['size comparison', "original: "+str(len(str(decrypted_message)))+" vs encrypted: "+str((len(str(bin(encrypted_message)))-2)//8)],
             ['encrypted message', str(encrypted_message)]
             ])

example_message = "Really Big string to encrypt Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam velit urna, tempor ut auctor non, efficitur eu purus. Pellentesque tincidunt sem dolor, et varius orci hendrerit a. Maecenas sed facilisis lacus. Suspendisse accumsan venenatis interdum. Quisque egestas, mauris aliquam consequat ultrices, justo elit mollis purus, vel lacinia lorem leo quis urna. Nullam vel lacinia nisi. Pellentesque dictum mi vel interdum semper. Praesent quis mattis libero, id rutrum quam. Etiam ultrices rhoncus urna, in venenatis eros vestibulum sed. In semper ipsum eu nulla congue, eu pharetra enim tincidunt. Sed ante ante, iaculis nec lorem eleifend, sodales dictum quam. Quisque in sapien placerat, luctus elit ornare, interdum tortor. Sed at congue purus, vel rhoncus erat. Morbi dignissim posuere consequat. Duis ornare nulla et felis tincidunt, vitae tempor ante sollicitudin. Nullam sagittis rhoncus metus et imperdiet. Sed vel scelerisque felis. Duis aliquam eleifend vehicula. Curabitur ut lacus justo. Proin mollis, est a pellentesque lacinia, nunc nisl ultrices justo, nec imperdiet purus risus vel mi. Pellentesque urna orci, mattis consequat quam a, porttitor sollicitudin eros. Ut vel porttitor nunc. Aenean vulputate ac nisi et dapibus. Nulla non ante magna. Aliquam posuere consectetur sem. Aliquam ut sem vel magna finibus accumsan. Aenean semper ac lacus a sollicitudin. Nulla neque sapien, ullamcorper at metus quis, sodales ultrices odio. Nunc ultricies auctor neque, vel molestie diam eleifend in. Fusce dolor odio, interdum eu lorem sit amet, hendrerit aliquam ex. Donec at neque malesuada, gravida ipsum in, suscipit ligula. Phasellus dolor nibh, euismod a leo sed, consequat vulputate ipsum. Pellentesque quis tellus quis lorem porta vulputate nec ac velit. Nunc eu vestibulum justo. Quisque feugiat ligula nec mollis finibus. Donec pharetra lacus consequat enim pellentesque malesuada. Pellentesque in auctor ligula, aliquet placerat erat. Nunc semper orci in fringilla porttitor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum vel ante ac lorem rhoncus ultrices hendrerit nec mi. Sed vel molestie magna, nec mattis justo. Fusce posuere sed urna eget rutrum. Nunc at dolor nec dui condimentum euismod."
key = Neza.generate_key()
encrypted_message, letters = Neza.encrypt(example_message, key)
decrypted_message = Neza.decrypt(encrypted_message, key, letters)

print_table([['key', str(key)],
             ['decrypted message', str(decrypted_message)],
             ['size comparison', "original: "+str(len(decrypted_message))+" vs encrypted: "+str((len(str(bin(encrypted_message)))-2)//8)],
             ['encrypted message', str(encrypted_message)]])