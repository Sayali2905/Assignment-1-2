num = int(input("Enter a three-digit number: "))

U = num % 10
num = num // 10

T = num % 10
num = num // 10

H = num

Reverse = U * 100 + T * 10 + H

print(f'Reverse = {Reverse}')