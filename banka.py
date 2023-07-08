import os
import time
from colorama import Fore, Back, Style

class bankaHesap:
    def __init__(self, hesap_no, bakiye):
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def para_yatir(self):
        soru = int(input("Lütfen yatırmak istediğiniz tutarı giriniz: "))
        self.bakiye += soru
        print(f"{self.hesap_no} numaralı hesap yeni bakiye miktarınız {self.bakiye}₺")
        os.system('cls')

    def para_cek(self):
        soru = int(input("Lütfen çekmek istediğiniz paranın miktarını giriniz: "))
        if self.bakiye >= soru:
            self.bakiye -= soru
            os.system('cls')
            print(
                f"{self.hesap_no} numaralı hesaptan {soru}₺ para çekildi yeni bakiyeniz {self.bakiye}₺")
            time.sleep(2)
        else:
            os.system('cls')
            print(f"Yetersiz bakiye, ana menüye yönlendiriliyorsunuz...")
            time.sleep(2)

    def hesap_durumu(self):
        print(f"{self.bakiye}₺")


banka = bankaHesap("000001", 0)

def main():
        os.system('cls')
        try:
            while True:
                print(f"""
                    {Fore.MAGENTA}Seçenekler
     {Fore.YELLOW}Bakiye: {banka.bakiye}₺
     {Fore.RED}Hesap No: {banka.hesap_no}

            {Fore.GREEN}1) Para Yatır
            2) Para Çek
            0) Çıkış
            """)
                soru = int(input(Fore.BLUE + "Lütfen bir seçenek seçiniz: "))
                if soru == 1:
                    banka.para_yatir()
                elif soru == 2:
                    banka.para_cek()
                elif soru == 0:
                    break
                else:
                    os.system('cls')
                    print("Geçersiz seçenek!")
        except ValueError:
            print("hatalı tuşlama")
        except KeyboardInterrupt:
            print("")
main()
