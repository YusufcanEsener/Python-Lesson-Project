x="global"
def myFunc():
    y="local"
    global x
    x=x*2
    print(x)
    print(y)
myFunc()