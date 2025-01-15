h,m,s = input("Input: ").split(":")
h = int(h)
m = int(m)
s = int(s)

if h >= 00 and h <= 23:
    if m >= 00 and m <= 59:
        if s >= 00 and s <= 59:
            th = h * 60 * 60
            tm = m * 60
            total = th + tm + s
            print("The number of seconds = %d" %total)

        else:
            print("Invalid time")
    else:
        print("Invalid time")
else:
    print("Invalid time")