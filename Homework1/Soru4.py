import math

#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
# Kullanıcıdan dairenin yarıçapını alma
yariCap = float(input("Dairenin yarıçapını girin: "))

# Dairenin alanını hesapla (π * r^2)
alan = math.pi * yariCap ** 2

# Dairenin çevresini hesapla (2 * π * r)
cevre = 2 * math.pi * yariCap


print("Dairenin Alanı: {:.2f}".format(alan))
print("Dairenin Çevresi: {:.2f}".format(cevre))