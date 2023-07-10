from colorama import Fore
import random
import time

secilen = []


def oyunu_baslat():

    secenekler = ["Taş", "Kağıt", "Makas"]
    oynanan_oyun = 0
    kazanilan_mac = 0

    def olasilik_hesapla():
        if (oynanan_oyun == 0 and kazanilan_mac == 0):
            return '0'
        else:
            return round(kazanilan_mac / oynanan_oyun * 100, 2)

    def robotun_sectigi():
        secilen_robot = random.choice(secenekler)
        secilen.append(secilen_robot.strip())

    try:
        while True:
            print("""
                        {}Tas Kagıt Makas Oyununa Hos Geldiniz !
                  
            {}Kazanma Olasılığınız: %{}
            Toplam Oynalılan Oyun: {}
            Kazanılan Maçlar: {}    
            """.format(Fore.RED, Fore.LIGHTWHITE_EX, olasilik_hesapla(), oynanan_oyun, kazanilan_mac))
            soru = str(input(Fore.GREEN + "Taş mı, Kağıt mı, Makas mı? (Çıkış yapmak için 'q' tuşuna basınız): ").title())

            robotun_sectigi()
            
            if soru.lower() == 'q':
                break
            
            if not soru in secenekler:
                print(Fore.LIGHTRED_EX + "Lütfen 'Taş, Kağıt, Makas' seçeneklerinden birisini yazınız.")
                return

            if (soru == 'Taş' and secilen[0] == 'Makas') or (soru == 'Kağıt' and secilen[0] == 'Taş') or (soru == 'Makas' and secilen[0] == 'Kağıt'):
                print(Fore.LIGHTYELLOW_EX + "Tebrikler, kazandınız ! Robotun seçimi: {}".format(secilen[0]))
                oynanan_oyun += 1
                kazanilan_mac += 1
                time.sleep(2)
            elif soru == secilen[0]:
                print("Berabere !")
                oynanan_oyun +=1
                time.sleep(2)
            else:
                print(Fore.RED + "Maalesef, kazanamadınız. Robotun seçimi: {}".format(secilen[0]))
                oynanan_oyun +=1
                time.sleep(2)
            olasilik_hesapla()
            secilen.clear()
    except ValueError:
        print("\nhatalı tuşlama")
    except KeyboardInterrupt:
        print("\nhatalı tuşlama")

if __name__ == '__main__':
    oyunu_baslat()
