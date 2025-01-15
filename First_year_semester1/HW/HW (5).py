def Word_count(d,x):
    for j in x:
        if j not in d:
            d[j] = 1
        else:
            d[j] += 1
a = 0
b = 0
c = 0
d = {}
while True:
    x = input("Enter a line (or 'END' to finish): ").lower()
    if x == "end":
        break

    x = x.replace(',', '').replace('.', '')
    x = x.split()
    Word_count(d,x)

for v in d.values():
    if v >= 1 and v <= 2:
        a += 1
    elif v >= 3 and v <= 4:
        b += 1 
    elif v > 4:
        c += 1
        
print("1. Number of words that appear once or twice: %d" %a)
print("2. Number of words that appear three and four times: %d" %b)
print("3. Number of words that appear more than four times: %d" %c)

#print(d)
#print(type(d))