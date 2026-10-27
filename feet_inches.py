ft = float(input("Enter the distance in Feet:"))
inches = float(input("Enter the distance in Inches:"))

#Convert feet into inches
total_inches =  (ft * 12) + inches

#Convert total_inches into centimeters
total_cm = total_inches * 2.54

#Convert cm into m
meter = total_cm / 100

#cm
cm = total_cm % 100

print(f'Meter = {meter}')
print(f'Centimeter = {cm}')