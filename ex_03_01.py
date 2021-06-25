hrs = raw_input("Enter hours: ")
h = float(hrs)

pay = raw_input("Enter pay: ")
p = float(pay)

if(h <= 40):
    pay = h*p
elif(h > 40):
    pay = 40*p + (h-40)*p*1.5
print(pay)
