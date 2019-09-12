a=0
int(a)
while a <= 100:
    a += 1
    if a%10 == 7 or a%7 == 0 or a//10 == 7:
        continue
    if a == 101:
        break
    print(a) 
