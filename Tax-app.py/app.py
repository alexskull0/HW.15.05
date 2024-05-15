from tax import calculateTax
from os import system

system('cls')

amount_of_money = 1500
procent = 15
purpose = 'salary'

result = calculateTax(amount_of_money, procent, purpose)

print(f'final sum is {result[0]}')
print(f'original value {result[1]}')
print(f'procent {result[2]}')
print(f'it was taken from {result[3]}')
