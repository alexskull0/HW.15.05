def inputInt( message ):
    value = int(input(message))
    return value

def inputFloat( message ):
    value = float(input(message))
    return value

def inputBoolean( message ):
    value = bool(input(message))
    return value

n = inputInt("Enter the first integer: ")
m = inputInt("Enter the second integer: ")

print( n + m )