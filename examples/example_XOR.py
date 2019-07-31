import XOR

message = "This is literally just an XOR cipher. Simple and straight-forward"
key = 0b011010110101010101010100100101101101011011101
enc = XOR.encrypt(message, key)
print(hex(enc))
dec = XOR.decrypt(enc, key)
print(dec)