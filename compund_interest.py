P = float(input("Enter Principal amount (P): "))
T = float(input("Enter Time in years (T): "))
R = float(input("Enter Rate of Interest (R): "))

Amount = P * (1 + R / 100) ** T

Compund_Interest = Amount - P

print(f'Compound Interest = {Compund_Interest}')
print(f'Total Amount = {Amount}')