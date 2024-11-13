#Recursion-Revursive function
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))
x=int(input("bir sayı giriniz:"))
print(factorial(x))