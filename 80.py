def outer():
    x="local"
    print("outer :",x)
    def inner():
        #nonlocal x
        x="nonlocal"
        print("inner: ",x)
    inner()
    print("outer :",x)
outer()