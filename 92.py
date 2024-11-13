def harfbul(aylar):
    for harf in aylar:
        if(harf[0]=='m'):
            print(harf)
aylar=["ocak","şubat","mart","mayıs","haziran","temmuz","aralık"]
harfbul(aylar)
print(list(filter(lambda x:x[0]=='m',aylar)))
deneme="şuan dışarıda kar yağıyor"
print(list(map(lambda x:len(x),deneme.split())))#sesli harfleri ve sessiz harfleri yazdır
sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
sesli_harf_sayisi = len(list(filter(lambda x: x.lower() in sesli_harfler, deneme)))
sessiz_harf_sayisi = len(list(filter(lambda x: x.lower() in sessiz_harfler, deneme)))
print("Sesli harf sayısı:", sesli_harf_sayisi)
print("Sessiz harf sayısı:", sessiz_harf_sayisi)
