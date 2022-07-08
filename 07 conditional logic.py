
#logical operators are either "true or false" or "yes or no" or "0 or 1"
# equal to                  ==
# not equal to              !=
# less than                 <
# greater than              >
# less than and equal to    <=
# GREATER than and equal to >=

# is 4 equal to 4
print(4==4)   #output are ture
print(4!=4)   #output are false
print(4>3)   #output are ture
print(3>6)   #output are false
print(3<=4)   #output are ture
print(5>=4)   #output are ture
#application of logical operators
hamad_age=4
age_at_school=5
print(hamad_age==age_at_school)

#inout funcaton and logical operator 
age_at_school=5
hamad_age=input("how old is hamad") #input funcation
hamad_age=int(hamad_age)          # it is used to convert string to int
print(type(hamad_age))
print(hamad_age==age_at_school)
