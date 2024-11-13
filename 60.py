class Error(Exception):
    pass
class ValueTooSmallError(Error):
    pass
class ValueTooLargeError(Error):
    pass


number=10
while True:
    try:
        i_num=int(input("enter a number: "))
        if i_num<number:
            raise ValueTooSmallError
        elif i_num>number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("valuetoosmall error")
    except ValueTooLargeError:
        print("valuetoolargeerror")