class urun_cikar:
    def __init__(self, sepet):
        self.sepet = sepet

    def cikar(self):

        if not self.sepet:
            print("Sepetiniz zaten boş")
            return

        print("\n Sepetinizdeki ürünler şunlardır:")
        for index, urun in enumerate(self.sepet, start=1):
            print(f"{index}. {urun}")


        
        urun = input("Çıkarmak istediğiniz ürünü girin....: ")
        
        if urun in self.sepet:
            self.sepet.remove(urun)
            print(f"{urun} ürünü sepetinizden çıkarıldı.")
        else:
            print("Girilen ürün sepette bulunamadı")
    
        