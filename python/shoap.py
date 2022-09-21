sum=0
while(True):
    userinput  =   int(input("enter the price: \n"))
    if(userinput!='q'):
        sum =   sum +   int(userinput)
        print(f"order total with last value: {sum}")
    else:
        print(f"your bill total is{sum}. thanks for using ounr application ")
        break