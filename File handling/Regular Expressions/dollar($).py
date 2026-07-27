# find names end with h
import re

names=['ramesh','kishore','rajesh','rakesh','nk','harsha']
for name in names:
    m=re.search(r'h$',name)
    if m:
        print(name)
