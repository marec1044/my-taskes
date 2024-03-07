def market():
    v=int(input("for the casher enter the product price: "))
    print("welcome")
    s=int(input("if you are student enter 1, or not enter 2 : "))
    o=int(input("if you are orphan enter 1, or not enter 2 : "))
    c=int(input("the country\ for egypt 1, another 2 :  "))
    if s==1 and o!=1 and c==2:
        print("your price is: ", int(v-((10/100)*v)))
    elif s==1 and o==1 and c==2:
        print(" your price is: ", int(v-((20/100)*v)))
    elif s==2 and o==2 and c==2:
        print("your price is:", v)
    elif s==1 and o==1 and c==1:
        print("your price is: ", int(v-((30/100)*v)))
    elif s==2 and o==2 and c==1:
        print("your price is: ", v)
    elif s==1 and o==2 and c==1:
        print("your price is: ", int(v-((20/100)*v)))
    else:
        print("buy from another market :) ")
market()