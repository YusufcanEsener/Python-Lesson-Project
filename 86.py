def power(x,n):
    if n ==0:
        return 1
    else:
        return x*power(x,n-1)
#print(power(2,7))
#num1=power(7)
#num2=num1(2)
#print(num2) bunları çalıştır
num1=int(input("üssü alınacak sayıyı giriniz: "))
num2=int(input("üssü giriniz: "))
print(power(num1,num2))