import xml.etree.cElementTree as ET


tree= ET.parse('xml files/students.xml')
root=tree.getroot()
print(root.tag)
print(root.attrib)
for child in root:
    print(child.tag)

for name in root.iter("name"):
    print(name.text)

for age in root.iter("age"):
    print(age.text)

for subject in root.iter("subject"):
    print(subject.text)
