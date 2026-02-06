#QQ WAP to display minimum and maximum values in a dictionary

d1={1:2,2:90,3:50}

print("For keys")
val1=d1.values()    #list m ho gaya
print(val1)

maximum=max(val1)
print("maximum = ",maximum)

minimum=min(val1)
print("minimum = ",minimum)

print("For Values ")

val2=d1.keys()
maximum=max(val2)
print("maximum = ",maximum)

minimum=min(val2)
print("minimum = ",minimum)


