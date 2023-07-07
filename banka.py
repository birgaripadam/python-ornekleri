import os
import time


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
                f"{self.hesap_no} numaralı hesaptan {soru}₺ para çekildi yeni bakiyeniz {self.bakiye}")
        else:
            os.system('cls')
            print(f"Yetersiz bakiye, ana menüye yönlendiriliyorsunuz...")
            time.sleep(2)

    def hesap_durumu(self):
        print(f"{self.bakiye}₺")

    def main(self):
        os.system('cls')
        try:
            while True:
                print(f"""
                    Seçenekler
     Bakiye: {self.bakiye}₺
     Hesap No: {self.hesap_no}

            1) Para Yatır
            2) Para Çek
            0) Çıkış
            """)
                soru = int(input("Lütfen bir seçenek seçiniz: "))
                if soru == 1:
                    self.para_yatir()
                elif soru == 2:
                    self.para_cek()
                elif soru == 0:
                    break
                else:
                    print("Geçersiz seçenek!")
        except ValueError:
            print("hatalı tuşlama")
        except KeyboardInterrupt:
            print("")


banka = bankaHesap("000001", 0)
banka.main()
