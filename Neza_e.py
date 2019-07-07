

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

def turn(message, bin_passcode):
    #get the necessary imputs from the widget
    message = message.upper()
    bin_passcode = str(bin_passcode)
    #make the message (turn the letters into numbers, copy them without separation into a number [list], join the list and turn the integer of the list into binary)
    bit_message = []
    for letter in message:
        location = int(alphabet.index(letter))
        bit_message.append(str(location))
    for item in bit_message:
        new_bit = []
        location = int(bit_message.index(item))
        if (len(bit_message[location]) != 2):
            bit_message[location] = "0" + bit_message[location]
        for letter in bit_message[location]:
            new_bit.append(letter)
        correct_bin = "".join(new_bit)
        bit_message[location] = correct_bin
    bit_message = "".join(bit_message)
    bit_message = turn_to_valid(bit_message)
    #make passcode binary
    bin_passcode = turn_to_valid(bin_passcode)
    #check wether the message and password are the same length. If not, repeat or delete from password until they are the same length
    if (len(bin_passcode) < len(bit_message)):
        loop_count =[]
        for i in range(len(bit_message)- len(bin_passcode)):
            bin_passcode = bin_passcode + bin_passcode[len(loop_count) + 2]
            loop_count.append("g")
    elif len(bin_passcode) == len(bit_message):
        return
    else:
        temp_bin_pass = []
        temp_bit_mess = []
        for c in bin_passcode:
            temp_bin_pass.append(c)
        for c in bit_message:
            temp_bit_mess.append(c)
        while (len(temp_bin_pass) != len(temp_bit_mess)):
            temp_bin_pass.pop()
        bin_passcode = "".join(temp_bin_pass)
    #remove the '0b' from both message and passcode
    bin_passcode = no_bin_t(bin_passcode)
    bit_message = no_bin_t(bit_message)
    #this is a new binary number. basically the XOR of the message and passcode
    new_message = []
    for i in range (len(bit_message)):
        if (bit_message[i] == '1' and bin_passcode[i] == '1'):
            new_message.append("0")
        elif (bit_message[i] == '0' and bin_passcode[i] == '0'):
            new_message.append("0")
        else:
            new_message.append("1")
    #turn the new message to hexadecimal
    new_message = int("".join(new_message), 2)
    hex_new_message = hex(new_message)
    if hex_new_message[-1] == "L":
        hex_new_message = hex_new_message[:-1]
    new_message = str(hex_new_message)
    #the 'f and length of the message help you decrypt it
    new_message = new_message + "f" +  str(len(bit_message))
    return new_message
