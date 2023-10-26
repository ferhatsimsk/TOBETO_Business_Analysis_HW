#1-İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

fibonacciSerisi = [1, 1]

while len(fibonacciSerisi) < 20:
    yeniSayi = fibonacciSerisi[-1] + fibonacciSerisi[-2]
    fibonacciSerisi.append(yeniSayi)

print(fibonacciSerisi)