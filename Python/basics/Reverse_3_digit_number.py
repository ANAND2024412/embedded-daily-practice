num= int(input("enter the 3 digit number "))
a=num%10
num=num//10
b=num%10
num=num//10
c=num%10
num=num//10
revnum=(a*100)+(b*10)+c
print("The reversed number is ",revnum)
