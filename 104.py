class Cizgi:
    def __init__(self, kenar):
        self.kenar = kenar
    def cevre(self):
        return self.kenar*3
    def alan(self):
        return self.kenar*self.kenar
class Kare:
#üçgen seçiyorsa yükseklik isteyin kare üçgen dikdörtgen olsun kullanıcıdan istesin
    def __init__(self, boyut):
        self.boyut=boyut
        #net sınavda çıkacak 