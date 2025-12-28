num=int(input("Enter a number(4 digit or more): "))

numlen=0
t=num

while t>0:
    numlen=numlen+1
    t=int(t/10)

if numlen>=4:
    numlen=int(numlen/2)
    check=0
    while num>0:
        rem=num%10
        if check==numlen:
            midone=rem
        elif check==numlen-1:
            midtwo=rem
        num=int(num/10)

        check=check+1
    product=midone*midtwo
    print(f"The product of the middle numbers {midone} and {midtwo}  is ",product )
else:
    print("The numbers is less than four digit")
