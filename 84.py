def myFunc():
    x=20
    def anyFunc():
        global x
        x=25
    print(x)
    anyFunc()
    print(x)
myFunc()
print(x)