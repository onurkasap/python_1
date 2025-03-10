class urun_ekle:

    def __init__(self,sepet):
        self.sepet = sepet
        
    def ekle (self):
        urun = input("Eklemek istediğiniz ürünü yazınız....: ")
        self.sepet.append(urun)
        print(f"{urun} sepete eklendi.")
        