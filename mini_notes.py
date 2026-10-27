amt = 990

fh = amt // 500
amt = amt % 500
print(fh)
print(amt)

th = amt // 200
amt = amt % 200
print(th)
print(amt)

h = amt // 100
amt = amt % 100
print(h)
print(amt)

f = amt // 50
amt = amt % 50
print(f)
print(amt)

t = amt // 20
amt = amt % 20
print(t)
print(amt)

ten = amt // 10
amt = amt % 10
print(ten)
print(amt)

total_notes = fh + th + h + f + t + ten
print(total_notes)