from src import XOR
from src.utils import print_table

message = "This is literally just an XOR cipher. Simple and straight-forward"
key = 0b011010110101010101010100100101101101011011101
enc = XOR.encrypt(message, key)
dec = XOR.decrypt(enc, key)

print_table([['key', str(key)],
             ['decrypted message', str(dec)],
             ['encrypted message', str(hex(enc))],
             ['size comparison', "original: "+str(len(str(dec)))+" vs encrypted: "+str(len(str(enc)))]])