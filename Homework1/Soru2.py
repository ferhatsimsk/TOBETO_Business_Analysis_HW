#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz. 
# Kullanıcıdan mevcut maaş ve zam oranını alma
maas = float(input("Lütfen mevcut maaşınızı giriniz: "))
zamOrani = float(input("Lütfen zam oranını giriniz (% cinsinden): "))

zamOrani = zamOrani / 100

# Zamlı maaşı hesapla
zamliMaas = maas + (maas * zamOrani)

print("Zamlı Maaş:", zamliMaas)