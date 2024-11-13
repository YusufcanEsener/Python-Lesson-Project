def fun(*args):
    print(args)
L=[1,2,3,4,5,6]
fun(*L)
D={'b':5,'c':7}
def func(**D):
    print(D)
func(**D)