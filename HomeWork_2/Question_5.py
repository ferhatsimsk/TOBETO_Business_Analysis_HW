#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

#Kullanıcıdan sayı al
sayi = int(input("Bir Sayı Girin: "))
bolen = 2 #Başlangıç bölenini temsil eder ve asal çarpanları kontrol etmek için 2'den başlar.
print(sayi, "Sayısının Asal Çarpanları:") #Asal Çarpanları ekrana yazdırır.
while bolen <= sayi: #bölen'in sayı'den küçük veya eşit olduğu sürece döngünün devam edeceğini belirtir. 
    if sayi % bolen == 0: #sayı'nin bölen'e bölündüğünü kontrol eder. Eğer bu koşul sağlanıyorsa bolen sayısı, sayi'nin bir çarpanıdır.
        print(bolen) 
        sayi //= bolen #Sayı'yı bölen'e böler. Buda sayı'nın bu çarpana bölünmüş halidir 
    else:
        bolen += 1 #Eğer sayı bölen'e bölünmüyorsa, yani bölen bir çarpan değilse,bölen += 1: bolen değeri bir arttırılır. Bu da bir sonraki çarpana(eğer varsa) geçmek için kullanılır.