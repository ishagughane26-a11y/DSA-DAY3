# 1.maximum consecutive ones
#i/p=[1,1,0,1,1,1,0,1,1,1,1]       o/p=4

# Maximum Consecutive Ones

# arr = [1,1,0,1,1,1,0,1,1,1,1]
# count = 0
# max_count = 0
# for i in arr:
#     if i == 1:
#         count += 1
#         if count > max_count:
#             max_count = count
#     else:
#         count = 0
# print(max_count)

# TCS QUESTION
#count sustring in a string
#i/p= "abababab" and "ab"       o/p=4

#while loop  : while condition: 
# statement
#  inc/dec
# i=1
# while i<=5:
#    print(i)
#    i+=1
    
str= "abababab"
count=0
for i in str:
    if i=="a":
       prev="a"

    if i=="b" and prev=="a":
      count +=1
      prev="b"

print(count)