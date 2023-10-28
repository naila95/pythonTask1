

aliram= input("Aliram (AZN , USD , EUR): ")
satiram= input("Satiram (AZN , USD , EUR): ")
mebleg = int(input("Mebleg: "))

if aliram == "AZN" and satiram =="USD":
    print(mebleg/1.7)
elif(satiram=='USD' and aliram == 'AZN'):
    print(mebleg*1.7)
elif(satiram=='AZN' and aliram == 'EUR'):
    print(mebleg*1.9)
elif(satiram=='EUR' and aliram == 'AZN'):
    print(mebleg/1.9)
