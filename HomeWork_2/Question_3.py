#3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

sayi1 = int(input("Birinci Sayıyı Giriniz : "))
sayi2 = int(input("İkinci Sayıyı Giriniz : "))

# İki sayıdan hangisinin daha küçük olduğunu belirlemek için kullanılır
if (sayi1>sayi2):
    kucukSayi = sayi2
else:
    kucukSayi = sayi1
for i in range(1,kucukSayi+1): #Küçük sayıya kadar olan sayılar için bir for döngüsü yazılır.
    if (sayi1 % i==0) and (sayi2%i ==0): #Eğer i, hem sayi1 hem de sayi2'ye tam bölünen bir sayı ise, bu sayı EBOB'dur.Ve EBOB olarak yazdırılır.
        ebob = i

print("Ebob = ",ebob)
print("Ekok = ", (sayi1*sayi2)//ebob) #EKOK, iki sayının çarpımının EBOB'a bölünmesiyle bulunur ve ekrana yazdırılır.