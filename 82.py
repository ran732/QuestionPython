#Mutable Operation of dictionary

#Adding item inside dictionary
student={101:'naresh'}
print(student)
student[102]='suresh'  #add
print(student)
student[103]='ramesh'  #add
print(student)


# Q1. Arrange the values in a dictionary in ascending order
# ex:
#     Original Dictionary ={1:25,2:21,3:23}
#     Expected Output=[21,25,32]

odict = {1:25,2:21,3:23}
val=list(odict.values())
output=(sorted(val))
print(output)


