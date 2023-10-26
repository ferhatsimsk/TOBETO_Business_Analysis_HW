#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
#Kullanıcıdan sayı al
sayi=int(input("Sayıyı Girin : "))

if sayi > 1:  #Sayı 1'den büyükse, asal sayı kontrolü yapabilir.
   
   for i in range(2,sayi): # 2'den başlayarak sayının kendisine kadar olan tüm sayıları dönen bir for döngüsüdür.
       if (sayi % i) == 0: # Eğer sayı, döngüdeki bir sayıya tam bölünebiliyorsa bu durumda sayı asal değildir.
           print(sayi," Asal Sayı Değildir.")
           break #Eğer asal olmayan bir bölen bulunursa bu durumda artık diğer bölenlere bakmaya gerek kalmaz ve döngüden çıkar.
   else:
       print(sayi," Asal Sayıdır.")
 
else:
   print(sayi," Asal Sayı Değildir.")