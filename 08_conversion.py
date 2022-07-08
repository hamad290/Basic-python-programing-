x=10       #integer
y=10.2     #float
z="hello"  #string

#implicite type conversion
x=x*y
print(x,"type of x is " ,type(x))   # output are float because it conver integer to floart after operation
 
 #explicit type conversion
 age=input("what is your age")
age=int(age)
print(age,type(age))