deger = int(input("lutfen bir sayi giriniz: "))
#asal sayı bulma
x=deger-1

while x>1:
    if deger%x==0:
        print('{} sayisi asal degildir'.format(deger))
        break
    else:
        x-=1
else:
    print('{} sayisi asal sayidir'.format(deger)) 
