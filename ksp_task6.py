#datatypes in python
print(" ")
print("datatypes in python")
print(" ")
number1=6
number2=4.3
name="priya"
char='j'
bool=True
string="""dkwejfewkfmjdjmhdei ijeijdkdm djeidjekncehf"""
print(type(number1))
print(type(number2))
print(type(name))
print(type(char))
print(type(bool))
print(type(string))



#casting
print(" ")
print("casting in python")
print(" ")
print(float(number1))
print(int(number2))
print(str(number1))
print(str(number2))
print(type(float(number1)))
print(type(int(number2)))
print(type(str(number1)))
print(type(str(number2)))



#Strings
print(" ")
print("strings in python")
print(" ")
name1="sai priya"
print("priya" in name1)
print("hi" in name1)
print(name1[0:5])
print(name1[6:9])
print(name1[:5])
print(name1[6:])
print(name1[2:6])





#OPERATORS

#Arithematic operators
print(" ")
print("Arithematic operators")
print(" ")
number3=10
number4=2
print(number3+number4)
print(number3-number4)
print(number3*number4)
print(number3/number4)
print(number3%number4)
print(number3**number4)
print(number3//number4)


#Assignment operator
print(" ")
print("Assignment operators")
print(" ")
number5=20
number6=10
number7=12
print(number5)
number5+=2
print(number5)
number5-=3
print(number5)
number5*=6
print(number5)
number5/=3
print(number5)
number7%=2
print(number7)
number6//=5
print(number6)
number6**=3
print(number6)



#comparison operators
print(" ")
print("comparison operators")
print(" ")
print(number3==number4)
print(number3!=number4)
print(number3<number4)
print(number3>number4)
print(number3>=number4)
print(number3<=number4)



#logical operators
print(" ")
print("Logical operators")
print(" ")
print(number3 < 11 and number4 > 3)
print(number3 < 11 or number4 > 3)
print(not(number3 < 11 and number4 > 3))



#identity operators
print(" ")
print("Identity operators")
print(" ")
demo1=["sai","priya"]
demo2=["sai","priya"]
print(demo1 is demo2)
print(demo1 is not demo2)



#membership operators
print(" ")
print("Membership operators")
print(" ")
print("sai" in demo1)
print("sai" not in demo2)




#input funtion
print(" ")
print("input function")
print(" ")
name2=input("enter your name")
print(name2)
num=int(input("enter a number"))
print(num)
