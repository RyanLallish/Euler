a=1
b=1
c=600
while(a<1000 or b<1000 or c<1000):
    if((a**2+b**2)==(c**2) and (a+b+c==1000)):
        print(str(a)+" "+str(b)+" "+str(c))
    elif(a<1000 or b<1000 or c<1000):
        if(a**2+b**2==c**2):
            print(str(a)+","+str(b)+","+str(c))
        if(a<1000):
            a=a+1
        if(b<1000 and a==1000):
            a=1
            b=b+1
            """print("b cycle")"""
        elif(a==1000 and b==1000 and c>1):
            a=1
            b=1
            c=c-1
            print("c cycle")
print("done")
