n=int(input("enter a number: "))
binary=''

if n==0:
    binary =0
else:
    while n>0:
        rem=n%2
        binary = str(rem) + binary
        n=n//2

print("The Binary number is ", binary)
