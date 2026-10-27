cp = float(input("Enter the Cost Price of Book:"))
dis = float(input("Enter the Discount Percentage of the Book:"))

Discount = (cp * dis) / 100

sp = cp - Discount

print(f'Selling Price = {sp}')