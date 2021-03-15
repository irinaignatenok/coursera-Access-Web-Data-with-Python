sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please numeric input")
    quit()
print(fh, fr)
if fh > 40:
    reg = fr*fh
    over_time = fh - 40
    over_pay = over_time*10.50*1.5
    xp = reg+ over_pay
else:
    xp = fh*fr
print("Pay", xp)
