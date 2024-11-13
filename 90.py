def kayitekle(isim,soyisim,sehir,tel,meslek,ilce):
    kayit={}
    kayit["%s %s"%(isim,soyisim)]=[sehir,tel,meslek,ilce]
    for k,v in kayit.items():
        print(k)
        print("-"*len(k))
        for i in v:
            print(i)
kayitekle("ahmet","kömüş","silivri","321323232","öğrenci","çanta")
