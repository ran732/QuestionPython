
import sys
try:
   f=open('createtxt.txt','r')
   s=f.read()
   print(s)
   
except:
    t=sys.exc_info()
    print(t[0])   
finally:   
    f.close()