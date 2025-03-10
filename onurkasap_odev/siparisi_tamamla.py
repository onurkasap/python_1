class siparisi_tamamla:
    def __init__(self, sepet):
        self.sepet = sepet
    
    def siparis_tamamlama(self):
        if self.sepet:
            
            print("\n Sipariş tamamlanmıştır. Mutlu günlerde kullanınız")
            print("\n Hazırlanan siparişler....:\n")
            
            for index, urun in enumerate(self.sepet, start=1):
                print(f"{index}. {urun}")
                
            self.sepet.clear()
        else:
            print("Siparişiniz oluşturulamadı. Lütfen sepete ürün ekleyiniz!")