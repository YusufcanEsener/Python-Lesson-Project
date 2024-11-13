taban=int(input("taban sayısını giriniz: "))
üst=int(input("kaçıncı kuvveti olsun: "))
def kuvvet(taban,üst):
    if(taban==0 or üst==0):
        sonuc=1
        print(sonuc)
    else:    
        sonuc=taban**üst
        print(sonuc)
kuvvet(taban,üst)