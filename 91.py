def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  
num=int(input("bir sayı giriniz: "))
print(fibonacci(num))
