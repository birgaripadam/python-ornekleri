import time
import os

os.system('cls')
print("#"*30)
print("""
Lutfen bir secenek seciniz !
 1) Tek Sayi Bulma
 2) Cift Sayi Bulma
 0) Cikis
""")
print("#"*30)
print(""*30)

def tekMiCiftMi ():
    while True:
        soru = input("lutfen islem seciniz : ")
        if soru == '0':
            print("cikis yapiliyor...")
            time.sleep(1)
            quit()
        elif soru == '1':
            os.system('cls')
            sayi = int(input("lutfen bir sayi giriniz: "))
            if sayi%2==1:
                print("{} sayisi tek sayidir.".format(sayi))
                quit()
            else:
                print("{} sayisi tek sayi degildir.".format(sayi))
                quit()
        elif soru == '2':
            os.system('cls')
            sayi = int(input("lutfen bir sayi giriniz: "))
            if sayi%2==0:
                print("{} sayisi cift sayidir.".format(sayi))
                quit()
            else:
                print("{} sayisi cift sayi degildir.".format(sayi))
                quit()

tekMiCiftMi()
