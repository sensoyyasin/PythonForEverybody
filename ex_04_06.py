def computepay(h,r):
    if h > 40:
        return (40*r)+(h-40)*(r*1.5)
    else:
        return h*r

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")

hrs = float(hrs)
rate = float(rate)

p = computepay(hrs, rate)
print(p)
