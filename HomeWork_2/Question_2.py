#2-Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

#Kullanıcıdan sayı al
sayi = int(input("Bir sayı giriniz: "))

#1'den başlayarak sayıya kadar olan sayıları kapsayan bir döngü oluşturur.
#i'nin sayıya bölünüp bölünmediğini kontrol eder. Eğer bölünüyorsa, i sayının bir böleni olur.
#eğer i sayıya bölünen bir sayı ise, bu i değerini toplama ekler.
toplam = 0
for i in range(1, sayi):
    if sayi % i == 0:
        toplam += i

#Kullanıcıdan alınan sayının mükemmel sayı olup olmadığını kontrol eder ve ekrana sonuca göre aşağıdaki mesajlardan birisini yazdırır.
if toplam == sayi:
    print(f"{sayi} mükemmel bir sayıdır.")
else:
    print(f"{sayi} mükemmel bir sayı değildir.")