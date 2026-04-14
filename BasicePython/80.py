# Example:

sales={2010:45000,
       2011:56000,
       2012:65000,
       2013:67000,
       2014:75000}

print(sales)
yr=sales.keys()
for i in yr:
    print(i)
    
am=sales.values()
for i in am:
    print(i)    
    
y=sales.items()
for i in y:
    print(i)    