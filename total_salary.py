basic = float(input("Enter basic salary: "))

da = basic * 10 / 100
ta = basic * 12 / 100
hra = basic * 15 / 100

total_salary = basic + da + ta + hra

print(f'DA = {da}')
print(f'TA = {ta}')
print(f'HRA = {hra}')
print(f'Total Salary = {total_salary}')