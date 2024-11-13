eski_harfler=['a','c','d','e']#shallow copy
eski_harfler_copy=['a','c','d','e'] #deep copy
yeni_harf=eski_harfler
yeni_harfler_copy=eski_harfler.copy()
yeni_harfler_copy.append('y')
print(yeni_harfler_copy)
print(eski_harfler_copy)
