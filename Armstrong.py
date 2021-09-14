num=int(input("enter the number"))
sum=0
temp=num
c=len(str(num))
while temp>0:
    digit=temp%10
    sum=sum+digit**c
    temp=temp//10
if num==sum:
    print("yes This is armstrong number ")
else:
    print("NO This is not a armstrong number")