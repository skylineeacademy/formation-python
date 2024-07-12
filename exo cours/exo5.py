credit = int(input("combien de crédit a tu "))
if credit <= 10 :
    print("désolé la conversion est impossible")
else :
    conv = ((credit*2)/(credit-10))+3
    print ("vous obtener "+ str(conv) + " Dz")