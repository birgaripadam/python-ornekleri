soru = int(input("Lutfen bir sayi giriniz : "))
fakt = 1

#faktoriyel alma
for sayi in range(1, (soru+1)):
    fakt = fakt * sayi

print("sonuc: ", fakt)
