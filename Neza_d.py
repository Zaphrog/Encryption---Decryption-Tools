
global alphabet
alphabet = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X", "Y", "Z"]



def turn_to_valid(string):
    corrected_m = []
    string = bin(int(string))
    return string

def no_bin_t(string):
    no_bin = []
    for c in string:
        no_bin.append(c)
    for i in range(2):
        no_bin.pop(0)
    no_bin = "".join(no_bin)
    return no_bin

def decrypt(message, bin_passcode):
    # get the original length of message and remove it from the message and set the message and passcode to binary
    mess_list = []
    for c in message:
        mess_list.append(c)
    reversed_list = list(reversed(mess_list))
    every_f = []
    for item in reversed_list:
        if item == 'f':
            every_f.append(reversed_list.index(item))
    original_len_mess = []
    for i in range(every_f[0] + 1):
        original_len_mess.append(reversed_list[i])
    original_len_mess = list(reversed(original_len_mess))
    for i in range (len(original_len_mess)):
        mess_list.pop()
    message = "".join(mess_list)
    message = no_bin_t(message)
    bin_passcode = bin(bin_passcode)
    message = bin(int(message, 16))
    original_len_mess.pop(0)
    original_len_mess = "".join(original_len_mess)
    #make the message the same length as the original
    if ((len(message)-2) != int(original_len_mess)):
        or_message = []
        for c in message:
            or_message.append(c)
        for i in range (int(original_len_mess) - (len(message)-2)):
            or_message.insert(2, "0")
        message = "".join(or_message)
    #repeat password (or delete) until it is the same length as the essage
    if (len(bin_passcode) < len(message)):
        loop_count =[]
        for i in range(len(message)- len(bin_passcode)):
            bin_passcode = bin_passcode + bin_passcode[len(loop_count) + 2]
            loop_count.append("g")
    elif len(bin_passcode) == len(message):
        return
    else:
        temp_bin_pass = []
        temp_bit_mess = []
        for c in bin_passcode:
            temp_bin_pass.append(c)
        for c in message:
            temp_bit_mess.append(c)
        while (len(temp_bin_pass) != len(temp_bit_mess)):
            temp_bin_pass.pop()
        bin_passcode = "".join(temp_bin_pass)
    #get the new binary
    message = no_bin_t(message)
    bin_passcode = no_bin_t(bin_passcode)
    new_message = []
    for i in range (len(message)):
        if (message[i] == '1' and bin_passcode[i] == '1'):
            new_message.append("0")
        elif (message[i] == '0' and bin_passcode[i] == '0'):
            new_message.append("0")
        else:
            new_message.append("1")
    new_message = str(int("".join(new_message), 2))
    new_message_in_letters = []
    new_message_list = []
    #check wether the message needs to have a 0 added at the beginning
    for c in new_message:
        new_message_list.append(c)
    if (len(new_message_list) % 2 != 0):
        new_message_list.insert(0, "0")
    new_message = "".join(new_message_list)
    #make the new list with pairs of numbers
    new_message = [new_message[i:i+2] for i in range(0, len(new_message), 2)]
    #translate those numbers into letters
    for item in new_message:
        new_message_in_letters.append(alphabet[int(item)])
    new_message = "".join(new_message_in_letters)
    return (new_message)
