mult=1
total=0
while(mult<1000):
    print(str(mult))
    if(mult%3==0):
        total=total+mult
    if(mult%5==0):
        total=total+mult
    if(mult%5==0 and mult%3==0):
        total=total-mult
    mult=mult+1
print("answer" + str(total))
