import sqlite3 as db
baglan=db.connect("test.db")
#baglan=db.connect("c:/users/test.db") windows için erişim
imlec=baglan.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS ogrenci(isim,soyisim,numara)")
#CRUD D ATABASE İŞLEMLERİ
veriler=[
    ("mehmet","kale",12),
    ("yusuf","can",20),
    ("kerem","ak",11)
    ]
for i in veriler:
    imlec.execute('INSERT INTO ogrenci VALUES(?,?,?)',i)
baglan.commit()
imlec.execute("SELECT * FROM ogrenci")#yaptıklarımız olmuşmu diye bakmamıza yarıyor
yazdir=imlec.fetchall()
print(yazdir)