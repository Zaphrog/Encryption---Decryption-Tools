def compress(message):
    used_letters = []
    compressed = []
    compressed_int = 0
    msg_lst = []
    for c in message:
        if c not in used_letters:
            used_letters.append(c)
        msg_lst.append(c)
    for item in msg_lst:
        compressed.append(used_letters.index(item)+1)
    size = len(str(bin(len(used_letters))))-2
    for item in compressed:
        compressed_int = compressed_int << size
        compressed_int += item
    compressed = []
    while compressed_int > 0:
        letter = compressed_int % (2**8)
        compressed_int = compressed_int >> 8
        compressed.insert(0,chr(letter))
    compressed = ''.join(compressed)
    return (used_letters, compressed)



def decompress(message, letters):
    message_int = 0
    decompressed = []
    dc = ''
    size = len(str(bin(len(letters))))-2
    for i in message:
        message_int = message_int << 8
        message_int += ord(i)
    while message_int > 0:
        n = message_int % (2**size)
        message_int = message_int >> size
        decompressed.insert(0,n)
    for item in decompressed:
        item = letters[item-1]
        dc += item
    return dc

def test(message):
    letters, compressed = compress(message)
    print(compressed)
    dec = decompress(compressed, letters)
    print(dec)




