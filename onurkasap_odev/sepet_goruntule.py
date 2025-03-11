class sepet_goruntule:
    def __init__(self, sepet):
        self.sepet = sepet
    
    def goruntule(self):
        if self.sepet:
            print("\n Sepetinizdeki Ürünler:")
            print(", ".join(self.sepet))

        else:
            print("Sepetiniz boş durumda.")
    
