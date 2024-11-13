print("""
1) Toplama
2) Çıkarma
3) Çarpma
4) Bölme
""")
while True:
    try:
        secim = input("Seçiminizi yapın: ")

        s1 = int(input("Birinci sayıyı girin: "))
        s2 = int(input("İkinci sayıyı girin: "))
        

        if secim == '1':
            sonuc = s1 + s2
            print("Sonuç: " + str(sonuc))
        elif secim == '2':
            sonuc = s1 - s2
            print("Sonuç: " + str(sonuc))
        elif secim == '3':
            sonuc = s1 * s2
            print("Sonuç: " + str(sonuc))
        elif secim == '4':
            sonuc = s1 / s2
            print("Sonuç: " + str(sonuc))
        else:
            print("Geçersiz bir seçim yaptınız.")
    except ValueError:
        print("Hata: Geçerli bir sayı giriniz.")
    except ZeroDivisionError:
            print("Hata: Bölen sıfır olamaz.")
