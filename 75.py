#Global,Non-Local,Local Variables
#global:Bir fonksiyonun dışında yada global bir alanda tanımlanmış değişkenlere global değişken denir
#bir fonksiyonun içinden veya dışından erişilebilir halde olan değişkenlerdir
#örnek:
#local:local alanda(scope) yada bir fonksiyonun içinde tanınmış olan değişkenlere local(yerel) değişken denir
#non-local variable:iç içe geçmiş fonksiyonlarda(nested function) kullanılan değişkenlerdir.Local alanlarda tanımlanmazlar.
#Ne globalde ne de localde bulunurlar.non-local değişkenleri tanımlamak için "nonlocal" kelimesi kullanılır
x="Global"
def myFunc():
    print("x inside function",x)
myFunc()
print("x outside function",x)
