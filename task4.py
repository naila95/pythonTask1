
boy = float(input("Boyunuzu Daxil edin:"))
kutle = float(input("Kütləni Daxil edin:"))

bki = kutle / boy * boy

if bki < 18.5:
    print("Zeif") 
elif 25 > bki > 18.5:
    print("Normal")
elif 30 > bki > 25:
    print("Kilolu")
elif  bki > 30:
    print("Obez")