import time
import os

def mailKontrol ():
    soru = input("lutfen bir mail adresi giriniz (cikis yapmak icin '0' tusuna basiniz): ")
    if soru == '0':
        print("cikis yapiliyor...")
        time.sleep(0.5)
        quit()
    time.sleep(.1)
    os.system('cls')
    print("Kontrol ediliyor...")
    time.sleep(1)
    while (('@' in soru) and ('.' in soru)):
        print("Tebrikler, mail adresiniz dogrulandi! {}".format(soru))
        quit()
    else:
        print("Maalesef, mail adresiniz dogrulanamadi. Lutfen tekrar deneyiniz.")
        time.sleep(2)
        os.system('cls')
        return mailKontrol()
mailKontrol()
