sum = 0
Num = int(input("Enter a number: "))
temp = Num
while(Num):
    i = 1
    fact = 1
    r = Num % 10
    while i <= r :
        fact = fact * i
        i+= 1
    sum = sum + fact
    Num = Num//10
if sum == temp :
    print( "This is a strong number")
else:
    print( " This is not a strong number")