#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
# Kullanıcıdan üç sayı alma
sayi1 = float(input("1. Sayıyı girin: "))
sayi2 = float(input("2. Sayıyı girin: "))
sayi3 = float(input("3. Sayıyı girin: "))

# En büyük sayıyı bul
enBuyukSayi = max(sayi1, sayi2, sayi3)

print("En Büyük Sayı: {}".format(enBuyukSayi))