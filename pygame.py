import random
num = random.randint(1,10)
print(num)
tries =0
while True:
    guess= int(input("please guess your number "))
    if num==guess:
     print(f"you are right in {tries}")
     break

    elif num< guess:
       print("go a littel lower")
       tries+=1
    elif num > guess:
       print("go littel high")
       tries+=1
    else:
       tries+=1
       print("you are wroung")

     