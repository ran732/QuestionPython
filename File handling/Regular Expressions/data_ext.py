#Extrecting data from string

import re

str1='date of joining is 12-05-2026'
m=re.search(r'(?P<day>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})',str1)
print(m)

print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print()
print(m.group('day'))
print(m.group('month'))
print(m.group('year'))
print(m.group(1,2,3))

