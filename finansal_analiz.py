import math

altin_getiri = [2.1, 3.4, -0.8, 1.2, 2.5]
fon_getiri = [7.5, -4.2, 10.1, -2.5, 8.8]

ortalama_Altin = (sum(altin_getiri))/len(altin_getiri)
ortalama_Fon = (sum(fon_getiri))/len(fon_getiri) 

print("Altın bazında getiri ortalamamız: ",ortalama_Altin)
print("Fon bazında getiri ortalamamız: ",ortalama_Fon)


altin_fark_kare = [(x- ortalama_Altin)**2  for x in altin_getiri]
fon_fark_kare = [(x - ortalama_Fon)**2 for x in fon_getiri]

altin_sapma = math.sqrt(sum(altin_fark_kare)/len(altin_fark_kare))
fon_sapma = math.sqrt(sum(fon_fark_kare)/len(fon_fark_kare))

if(altin_sapma>fon_sapma):
    print("Altın yatırımının sapması büyük olduğu için daha risklidir.Sapması: ",altin_sapma)
else:
    print("Fon getirisinin sapması büyük olduğu için daha risklidir. Sapması: ",fon_sapma)


altin_verimlilik = ortalama_Altin/ altin_sapma
fon_verimlilik = ortalama_Fon/ fon_sapma

if(altin_verimlilik>fon_verimlilik):
    print("Risk başına en yüksek getiriyi ALTIN sağlıyor.")
else: 
    print("Risk başına en yüksek getiriyi Fon sağlıyor.")
