credit = int(input("combien de crédit a tu "))
long = len(str(credit))
if long < 5 :
 if credit <= 10 : 
     print("désolé la conversion est impossible")
 else :
     conv = ((credit*2)/(credit-10))+3
     print ("vous obtener "+ str(conv) + " Dz")
else :
   print("le nombre de crédit est trop grand")