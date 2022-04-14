lower = 1 #int(input("Enter the lower value:"))
upper = 250 #int(input("Enter the upper value:"))

f= open("primeNumber.txt","w+")

for number in range(lower,upper+1):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
 #           print(number)
            f.write(" %d\r\n" % (number+1))
f.close()
#print("Check the file primenumber.txt")
