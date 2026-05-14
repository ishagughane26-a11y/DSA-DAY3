#function
# def hello(): #called function
#     print("hello world")

# hello() #calling function
# hello()    

# def airthmatic():
#     a=int(input("Enter value of a:"))
#     b=int(input("Enter value of b:"))
#     sum=a+b
#     sub=a-b
#     div=a/b
#     mul=a*b
#     return sum,sub,div,mul
# #print(aithmatic())
# result=airthmatic()
# print("Airthmatic =",result)

#How many types of argument we pass in function? 
#  1.positional argumnet 2.keyword argument 3.default argument 4.varible length argument/variable number of argumemt

# def airthmatic(a,b):         
#     sum=a+b
#     sub=a-b
#     div=a/b
#     mul=a*b
#     return sum,sub,div,mul
# #print(aithmatic())

# #positional arguments

# result=airthmatic(5,5)
# print("Airthmatic =",result)


# 2.keyword argument
# def credential(username,passward):
#     if username==passward:
#         print("login succesfully")
#     else:
#         print("invalid credentials")
         
# credential(username="admin",passward="admin")         #calling function 
    
#3.default argument
# def cityName(city="Mumbai"):
#     print(city)
# cityName("Nagpur")
# cityName("Pune")
# cityName()    

#4. 4.varible length argument/variable number of argumemt
# def cityName(*name):
#     print(name)

# cityName("Nagpur","delhi","Mumbai","pune")    

#----------------------------------------------------------------------------------------------------------------
#MODULARITY APPROCH IN FUNCTION
import sys
def add():
    a=int(input("Enter value of A:"))
    b=int(input("Enter value of B:"))
    print(a+b)

def sub():
    a=int(input("Enter value of A:"))
    b=int(input("Enter value of B:"))
    print(a-b)

def div():
    a=int(input("Enter value of A:"))
    b=int(input("Enter value of B:"))
    print(a/b)

def mul():
    a=int(input("Enter value of A:"))
    b=int(input("Enter value of B:"))
    print(a*b)

while True:
    print("1.Addition")    
    print("2.Subtraction")
    print("3.Division")
    print("4.Multiplication")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice ==1:
        add() # calling function
    elif choice==2:
        sub()
    elif choice==3:
        div()  
    elif choice==4:
        mul()          
    elif choice==5:
        sys.exit()