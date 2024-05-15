from os import system
system('cls')

def wrap_brackets( text ):
  return "(" + text + ")"

def wrap_square_brackets ( text ):
  return '[[[' + text + ']]]'

def wrap_triang_brackets ( text ):
  return '<<<' + text + '>>>'

print(wrap_triang_brackets(wrap_square_brackets(wrap_brackets("12345"))))