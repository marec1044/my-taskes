country=input("enter your country: ")
state=input("are you student?: ")
o=input("are you orphan?: ") 
v=int(input("for the casher enter the price: "))
if country=="egypt":
   print(state)
   if state=="yes":
       print(o)
       if o=="yes":
           print("your price after discount is: ", int((v-((40/100)*v))))
       elif o=="no":
           print("your price after discount is: ", int((v-((30/100)*v))))
   elif state=="no":
        print("your price after discount is: ", int((v-((20/100)*v))))
elif country=="ksa":
    print(state)
    if state=="yes":
       print(o)
       if o=="yes":
            print("your price after discount is: ", int((v-((30/100)*v))))
       elif o=="no":
           print("your price after discount is: ",int((v-((20/100)*v))))
    elif state=="no":
        print("your price after discount is: ",int((v-((10/100)*v))))
elif country=="usa":
    print(state)
    if state=="yes":
        print(o)
        if o=="yes":
            print("your price  after discount is: ",int((v-((20/100)*v))))
        elif o=="no":
            print("your price  after discount is: ", int((v-((10/100)*v))))
    elif state=="no":
        print("your price after discount is: ", (v))
else:
    print("puy from another market")