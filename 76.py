def myFunc():
    global x
    x="global"
    print("x inside function",x)
myFunc()
print("x outside function",x)