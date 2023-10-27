

adlar=["Fidan","Lale", "Fatime","Sevinc"]

b= input("Ad daxil edin:")

if len(b)<=15:
  adlar.append(b)
  print("Ad Bazaya ugurla elave olundu")
  print(adlar)

elif b=="":
  print("Ad daxil etmediniz")

elif len(b)>15:
  print("Ad cox uzundur maksimum 15 herf")