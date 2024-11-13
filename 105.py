class Oyun:
    def __init__(self):
        self.enerji=150
        self.para=1000
        self.fabrika=3
        self.isci=10
    def Yazdir(self):
        print("enerji",self.enerji)
        print("para:",self.para)
        print("fabrika sayısı:",self.fabrika)
        print("işçi sayısı:",self.isci)
    def fabrikakur(self,miktar):
        if self.enerji>40 and self.para>100:
            self.fabrika+=miktar
            self.enerji=(self.enerji-(miktar*40))
            self.para=self.para-(miktar*100)
            print(miktar," adet fabrikanız kuruldu!")
        else:
            print("paranız yada enerjinin yetersiz")
oyun=Oyun()
oyun.Yazdir()
oyun.fabrikakur(2)
oyun.Yazdir()
oyun.fabrikakur(9)
oyun.Yazdir()
oyun.fabrikakur(2)