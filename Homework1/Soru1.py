#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
# Kullanıcıdan boy ve ağırlık bilgilerini alınması
boy = float(input("Lütfen boyunuzu (metre cinsinde) giriniz: "))
agirlik = float(input("Lütfen ağırlığınızı (kilogram cinsinde) giriniz: "))

# Vücut Kitle İndeksi hesaplanması
vki = agirlik / (boy ** 2)

print("Vücut Kitle İndeksi :", vki)