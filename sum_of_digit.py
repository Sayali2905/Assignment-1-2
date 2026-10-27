N = int(input("Enter a three-digit number: "))

U = N % 10
N = N // 10

T = N % 10
N = N // 10

H = N

Sum = H + T + U

print(f'Sum of digits = {Sum}')