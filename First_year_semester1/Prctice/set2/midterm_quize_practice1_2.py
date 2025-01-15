a,b = x = input("Please enter your information: ").split(",")

if a.isnumeric() and b.isalpha() or a.isalpha() and b.isnumeric():
    if a.isnumeric() and b.isalpha():
        a = int(a)
        if a >=0 and a<=120:    
            print("Your name is %s" %b)
            print("Your age is %s" %a)
        else:
            print("Please enter your complete information.")
    elif a.isalpha() and b.isnumeric():
        b = int(b)
        if b >=0 and b<=120:    
            print("Your name is %s" %a)
            print("Your age is %s" %b)
        else:
            print("Please enter your complete information.")
else:
    print("Please enter your complete information.")



#if a.isalpha() and b.isnumeric():
    #b = int(b)
    #if b >=0 and b<=120:    
       # print("Your name is %s" %a)
       #print("Your age is %s" %b)
   # else:
   #     print("Please enter your complete information.")
#else:
   # print("Please enter your complete information.")



