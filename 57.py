while True:
    try:    
        num1=int(input("birinci sayı giriniz:"))
        num2=int(input("ikinci sayıyı giriniz:"))
        result=int(num1)+int(num2)
        print(result)
    except ValueError:
        print("bir hata oluştu")
        