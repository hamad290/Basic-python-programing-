 #while and for loop
 # while loops
x=0
while(x<5):
    print(x)
    x=x+1 


    #for loop   is ma hum range da tai hai
    for x in range(5,10):
        print(x)


 #array
days = ["Mon","Tue","Wed","Thu","Fri"]

for d in days:
    if(d=="wed"):break #loop stops
    if(d=="wed"):continue #skips d it mean before  the wed and wed are skips are the loop will be start from Thu
    print(d)
    