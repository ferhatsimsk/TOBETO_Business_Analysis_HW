#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
# Kullanıcıdan bir sayı al
sayi = input("Bir sayı girin: ")

# Sayıyı tersten yazılmış haliyle karşılaştır.
tersSayi = sayi[::-1]

# Palindrom kontrolü yap
if sayi == tersSayi:
    print("{} bir palindrom sayıdır.".format(sayi))
else:
    print("{} bir palindrom sayı değildir.".format(sayi))