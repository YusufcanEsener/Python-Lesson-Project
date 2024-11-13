import sqlite3 as db
class Database:
    def __init__(self):
        try:
            self.baglan = db.connect('test31.db')
        except db.OperationalError:
            print("Veritabanı bağlantısı kurulamadı.")
            exit(1)
        self.cursor = self.baglan.cursor()

    def tablo_olustur(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS ogrenci \
                            (id INT PRIMARY KEY, \
                            isim CHAR(20), \
                            soyisim CHAR(50), \
                            numara INT)')

    def kayit_ekle(self):
        isim = input("Bir isim giriniz:")
        soyisim = input("Soy isim giriniz:")
        numara = int(input("Bir numara giriniz:"))
        self.cursor.execute("INSERT INTO ogrenci (isim, soyisim, numara) VALUES (?,?,?)", (isim, soyisim, numara))

    def kayit_listele(self):
        self.cursor.execute("SELECT * FROM ogrenci ")
        yazdir = self.cursor.fetchall()
        print(yazdir)

    def veritabani_kapat(self):
        self.baglan.commit()
        self.baglan.close()

    def kayit_guncelle(self):
        ogrenci_id = int(input("Güncellenecek öğrenci ID'sini giriniz: "))
        yeni_isim = input("Yeni ismi giriniz:")
        yeni_soyisim = input("Yeni soy ismi giriniz:")
        yeni_numara = int(input("Yeni numarayı giriniz:"))

        self.cursor.execute("UPDATE ogrenci SET isim=?, soyisim=?, numara=? WHERE id=?", (yeni_isim, yeni_soyisim, yeni_numara, ogrenci_id))

    def kayit_sil(self):
        ogrenci_id = int(input("Silinecek öğrenci ID'sini giriniz: "))
        self.cursor.execute("DELETE FROM ogrenci WHERE id=?", (ogrenci_id,))


def main():
    datab = Database()
    datab.tablo_olustur()

    while True:
        print("\n1. Kayıt Ekle")
        print("2. Kayıtları Listele")
        print("3. Kayıt Güncelle")
        print("4. Kayıt Sil")
        print("5. Çıkış")

        secim = input("Seçiminizi yapınız (1-5): ")

        if secim == "1":
            datab.kayit_ekle()
        elif secim == "2":
            datab.kayit_listele()
        elif secim == "3":
            datab.kayit_guncelle()
        elif secim == "4":
            datab.kayit_sil()
        elif secim == "5":
            datab.veritabani_kapat()
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()
