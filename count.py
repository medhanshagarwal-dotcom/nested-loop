n=input("Enter a word ")

c=input("Enter a charachter to search for ")

i=0
co=0

while (i<len(n)):
    if n[i]==c:
        co=co+1

    i=i+1

print(f"The character {c} has come {co} times in {n}")