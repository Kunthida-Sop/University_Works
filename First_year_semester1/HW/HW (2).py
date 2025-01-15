import math as m
start = input("Start number: ")
stop  = input("End number: ")
step = input("Step number: ")

numoflist = 0
prime = True
n =""
numprime = 0

if start.isnumeric():
    if stop.isnumeric():
        if step.isnumeric():
            start = int(start)
            stop = int(stop)
            step = int(step)
            if start >= 1 and step >=1:
                if stop > start:
                    for i in range(start, stop+1, step): #1 2 3 4 5 6 7 8 9 10
                        numoflist += 1
                        i = int(i)
                        if i == 1:
                            prime = False
                        if i > 1:
                            prime = True
                            for j in range(2, int(m.sqrt(i)+1)): # 2 3 4 5 6 7 8 9
                                if i%j == 0 :
                                    prime = False
                                    break

                        if prime:
                            n += str(i) + "*" + ", "
                            numprime += 1
                        else:
                            n += str(i) + ", "

                    print("Starting from %d and ending at %d with a step of %d, there are a total of %d numbers." %(start,stop,step,numoflist))
                    print("Among them, %d are prime." %numprime)
                    print("Numbers: %s" %n.strip(", ")) 
                else:
                    print("Input ERROR!!")   
            else:
                print("Input ERROR!!")
        else:
                print("Input ERROR!!")
    else:
        print("Input ERROR!!")
else:
    print("Input ERROR!!")
    