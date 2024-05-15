from os import system
system ('cls')

direction = input('enter the direction (h/v): ')
length = int(input('enter the length: '))

def drawLine(length, direction):
    if direction == 'h':
        print ('-' * length)
    elif direction == 'v':
        print('|' * length)

drawLine(length, direction)