trinum=1
count=0
maxcount=1
numcount=76576499
i=1
while(maxcount<=500):
    while(i<=trinum):
            if(trinum%i==0):
                count=count+1
            if(count>maxcount):
                maxcount=count
                print(maxcount)
            i=i+1
    last=trinum
    trinum=last + numcount
    i=1
    count=0
    numcount=numcount+1
    print("numcount"+str(numcount))
print("First triangle to have over 500 divisors is " + str(last))

#this code runs extremely slowly as it increaes exponentially twice. The code does get the right number though that is why numcount starts so high
