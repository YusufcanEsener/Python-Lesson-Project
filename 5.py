#if test_ifadesi:
    #durumlar(statement)
#nested if (iç içe geçmiş ifler)
num=int(input("bir sayı giriniz:"))
if num>=0:
    if num==0:
        print("sıfır")
    else:
        print("pozitiftir")
else:
    print("negatiftir.")