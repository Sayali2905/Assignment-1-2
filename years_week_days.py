days = int(input("Enter number of days: "))

Years = days // 365

days = days % 365

Weeks = days // 7

days = days % 7

print(f'Years = {Years}')
print(f'Weeks = {Weeks}')
print(f'Days = {days}')