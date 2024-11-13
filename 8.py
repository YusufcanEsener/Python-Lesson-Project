muzik=['pop','rock','caz']
for i in range(len(muzik)):
    print("bu müziği çok severim",muzik[i])
sayılar =[0,10,15]
for i in sayılar:
    print(i)
else:
    print('yazdıracak eleman kalmadı')
soyad='ahmet'
notlar={'ahmet':90,'Recep':80}
for öğrenci in notlar:
    if öğrenci==soyad:
        print(notlar[öğrenci])
        break
else:
    print('kayıtlı değil')
print(type(notlar))