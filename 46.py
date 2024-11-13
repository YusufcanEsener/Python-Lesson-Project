myset={1,2,4,5,6}
print(myset)
myset.discard(4)#discard ile setin içinde olmayan elemanı çıkarmaya çalışırsak hata vermez
myset.remove(6)#remove da ise hata verir olmayan eleman varsa
print(myset)