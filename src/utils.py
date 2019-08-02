
def print_table(data):
    dash = '-' * 40
    for i in range(len(data)):
        print('{:<24s}{:>5s}'.format(data[i][0],data[i][1]))
    print('')