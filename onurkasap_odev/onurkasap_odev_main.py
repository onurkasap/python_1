from urun_ekle import urun_ekle
from urun_cikar import urun_cikar
from sepet_goruntule import sepet_goruntule
from siparisi_tamamla import siparisi_tamamla

class main:

    def __init__(self):
        self.sepet = []
        self.urun_ekle=urun_ekle(self.sepet)
        self.urun_cikar=urun_cikar(self.sepet)
        self.sepet_goruntule=sepet_goruntule(self.sepet)
        self.siparisi_tamamla=siparisi_tamamla(self.sepet)

    def menu(self):
        while True:

            print("\n Yapmak İstediğiniz İşlemi Seçiniz: ")
            print("1. Ürün ekle")
            print("2. Ürün çıkar")
            print("3. Sepeti görüntüle")
            print("4. Siparişi Tamamla")
            print("5. Çıkış")


            secim = input(f"Seçiminizi giriniz (1-5):  ")

            if secim == "1":
                self.urun_ekle.ekle()
            elif secim== "2":
                self.urun_cikar.cikar()
            elif secim == "3":
                self.sepet_goruntule.goruntule()
            elif secim == "4":
                self.siparisi_tamamla.siparis_tamamlama()
            elif secim == "5":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Hatalı işlem yaptınız. Lütfen size tanımlanan işlemlerden seçiniz...")
        
if __name__ == "__main__":
    uygulama = main()
    uygulama.menu()


