# # find biggest number
# def findBiggestNumber(sampleArray):         #===>
#     biggestNumber =sampleArray[0]       # ====> O(1)

#     for index in range(1,len(sampleArray)): #   =======> O(N)

#         if sampleArray[index] > biggestNumber:    # ===========> O(1)

#             biggestNumber=sampleArray[index] #============= O(1)

#     print(biggestNumber)     #============= O(1)

# sampleArray = [5,7,9,2,3,4]     #============= O(1)
 
# findBiggestNumber(sampleArray)             #============= O(1) +O(1)+O(1)+O(1) +O(N)=O(N)

# def foo(array):
#     sum=0
#     product=1

#     for i in array :
#     sum+=i


# LINEAR SEARCH

# def linearSearch(array,target):
#     for i in range(0,len(array)): # i=0
#         if array[i] == target:
#             return i
#     return -1
    
# array=[1,2,3,4,8,7,9]
# target =7 #search the target value i.e 7
# result=linearSearch(array,target)
# if result==-1:
#     print("Target not found")
# else:
#     print("Target found at index:",result)

#Removing spaces from the string
#1.rstrip:to remove spaces from right hand side
#2.lstrip:to remove spaces from left hand side
#3.strip:to remove spaces both side
# city=input("Enter your city Name:")
# scity=city.strip()
# if scity=='Hyderabad':
#     print("Hello Hyderabadi..Adab")
# elif scity=="chennai":
#     print("Hello Madrasi...vanakkam")
# elif scity=='Banglore':
#     print("Hello kannadiga..Shubhodaya")
# else:
#     print("Your enterd city name is invalid")        

#ROW wise max value
# [[100,198,333,323],
# [122,232,221,111],
# [223,565,245,764]]    .
# mylist=[[100,198,333,323],
# [122,232,221,111],
# [223,565,245,764]] 

# newlist=[]
# for i in range(3):
#     j=0
#     max = mylist[i][j]
#     for j in range(4):
#         c_max=mylist[i][j]
#         if max < c_max:
#             max = c_max
#     newlist.append(max)
# print(newlist)      
# 
# 
# input=prashant*is*a*good*programmer
# output=****prashantisagoodprogrammer   
   
# name='prashant*is*a*good*programmer'
# newname=''
# val=''
# for i in name:
#     if i != "*":
#         newname +=i
#     else:
#         val+= i
# print(newname)
# print(str(val+newname))

#input=aaabbbbccceeeee
#outout=a3b4c3e5

str='aaabbbbccceeeee'
count=1
res="" 
for i in range(len(str)):
    if str[i] == str[i+1]
      count+=1
    else:
        result += s[i] + str(count)
        count = 1
result += str[-1] + str(count)

print(result)
