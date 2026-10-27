hours = float(input("Enter the Hours:"))
minutes = float(input("Enter the Minutes:"))
seconds = float(input("Enter the Seconds:"))

Hours = hours * 3600
Minutes = minutes * 60

Total_seconds = Hours + Minutes + seconds

print(f'Total Seconds = {Total_seconds}')