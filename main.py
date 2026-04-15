#print("namaste youtube we are learning python ")

#sher = "hhghg"
#a = 12
#b = True 
#print(type(sher)) 
 # string indexing  assing each elements of a sting
#a= "hello"
#print(a[0])
#string slicing
#s = "hii sarika"
#print(s[4::1])
# type conversion 
#a= 12 
#a = str(a)
#print (type(a))
  
#a = input(" please inter the number")
#print(a)

#money = int(input("please mummy give me money"))
#if money==10 : 
 #   print("i will buy chocobar ")
#else: 
  #  print(" i will buy wannila ")

#num = int(input("please tell your number"))
#if num%2 == 0:
 #   print("even number")
#else:
 #   print("odd number")

#t = int(input(" please tell the temperature "))
#if t< 0:
  #  print("extreme cold")
#elif t>=0 and t<10 :
   # print(very cold)
   # elif

#for i in range(16,0,-1):
    #print(i)

#for i in range(5,51,5):
 #   print(i)
#n = int(input("enter the table number"))
#for i in range(n,(n*10)+1,n):
  #  print(i)

#a = " hii sarika your krishna will always with you"
#for i in range(len(a)):
 #   print(a[i])

#a = "sarika kumari"
#for i in a:
  #  print(i)

#n = int(input("please tell your number"))
#for i in range(n):
 #   print("hello world")
  
#n = int(input("please tell your  natural number"))
#for i in range(1,n+1,1):
 #   print(i)

# reverse for loop 

#n = int(input("please enter your number"))
#for i in range(n,0,-1):
 #   print(i)

#take number as input and prints its table 

#n = int(input("please enter your num"))
#for i in range(n,n*10+1,n):
  #  print(i)
#sum up to n term 

# s = int(input("which num sum u want pls enter"))
# sum =0

# for i in range(1,s+1):
#   sum = sum+i
# print(f"yoursum is {sum}")
# print all the factors of a number 

# s = int(input("which num factor u want pls enter"))
# fac =1

# for i in range(1,s+1):
#   fac = fac*i
# print(f"your factor is {fac}")
# print the sum of all even and odd number in a ranhe separtely

# n = int(input("tell your number"))
# even =0
# odd =0
# for i in range(1,n+1):
#     if i%2==0:
#         even = even+i
#     else:
#         odd= odd+i

# print(f"your even and odd sum is {even} , {odd}")


# print all the factor of a number 

# n = int(input("enter the number"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
# accept a number and check if it is a perfect number or not 

# n = int(input("check your number is perfect or not"))
# sum =0
# for i in range(1,n):
#     if n%i ==0:
#         sum = sum+i
        
# if sum==n:
#     print("your number is perfect ")
# else:
#     print("not perfect") 

   # check wherthr the number is prime or not 

# n = int(input("enter your number"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count= count+1
# if count==2:
#     print(" your number is a prime number")
# reverse a string 

# a = "sarika"
# b=""
# for i in range(len(a)-1,-1,-1):
#     b= b+a[i]
# print(b)
# check string is palindrame or not

# a ="naman"
# b =""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# if b == a:
#     print("your string is palindrome")
# else:
#     print("not a palindrome")

# a = "sdfsogn12413@#&%^&U"

# char=0
# dig =0
# spchr=0
# for i in a:
#     if i.isdigit():
#         dig +=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr+=1

# print(f"your digits are{dig}\nyour alphabets are {char}\n your specialchar are{spchr}")
    
# sepate each digit of a number 

# a = 256
# while a>0:
#     print(a%10)
#     a=a//10

# reverse a number 

# a = 256
# rev =0
# while a>0:
#     rev=rev*10+a%10
#     a=a//10
# print(rev)

#palindrome number 
a = int(input("enter the number"))
copy=a
rev =0
while a>0:
    rev=rev*10+a%10
    a=a//10
if copy==rev:
    print("palindrome number")
else:
    print("not ")
