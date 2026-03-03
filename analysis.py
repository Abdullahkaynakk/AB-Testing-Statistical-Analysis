import math

# Grup A (Eski Tasarım) Verileri 

ziyaretci_A = 1000
satis_A = 50

# Grup B (Yeni Tasarım) Verileri 

ziyaretci_B = 1000
satis_b = 75

OranA = satis_A/ziyaretci_A 
OranB = satis_b/ziyaretci_B

print("Eski Tasarım Oranı:", OranA)
print("Yeni Tasarım Oranı:", OranB)


if(OranA>OranB):
    sonuc1 = OranA-OranB
    print("Eski Tasarım oranı Daha büyüktür",sonuc1)
else:
    sonuc2 = OranB-OranA
    print("Yeni Tasarım Oranı daha Büyüktür : ", sonuc2)


se_a = math.sqrt((OranA*(1-OranA)) / ziyaretci_A)
print("A Grubu Standart Sapma Hatası : ",se_a)

se_b = math.sqrt((OranB*(1-OranB))/ziyaretci_B)
print("B Grubu Standart Sapma Hatası : ", se_b)

se_fark = math.sqrt(se_a**2 + se_b**2)
print("Gruplar Arasındaki Toplam Standart Hata: ",se_fark)

z_skoru = (OranB- OranA)/ se_fark

if(z_skoru>1.96):
    print("İstatiksel olarak anlamlı bir artış vardır. Yeni Tasarım : ",OranB)
else:
    print("Artış şans eseri olabilir,daha fazla veri lazım.")

    