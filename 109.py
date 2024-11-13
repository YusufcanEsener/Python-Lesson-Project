import sqlite3 as db
baglan=db.connect("test.db")
imlec=baglan.cursor()
#CRUD D ATABASE İŞLEMLERİ
isim=input("İsim giriniz:")
imlec.execute("SELECT * FROM ogrenci WHERE isim= '%s'"%isim)
yazdir=imlec.fetchone()
if yazdir:
    print("bu isimde bir kayıt var")
else:
    print("bu isimde bir kayıt yoktur")