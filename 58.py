
import sys
randomlist=['a',0,2]
for entry in randomlist:
    try:
        print('The entry is: ',entry)
        r=1/int(entry)
        break
    except:
        print("ooppss",sys.exc_info()[0],"occured")
        print("next entry")