grenze = int(input("Bitte Grenze eingeben : "))

for a in range(2, grenze+1):
    for b in range(2, a+1):
        if ((a%b==0) and (a!=b)):
            break
        if(a==b):
            print(a)

out = input("Press ENTER to quit...")