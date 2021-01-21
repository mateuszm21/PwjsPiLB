from xml.dom import minidom

file = minidom.parse("carbs.xml")
carbs = file.getElementsByTagName("carb")

for carb in carbs:
    typeNode = carb.getElementsByTagName("type")[0].childNodes[0]
    typeNode.nodeValue = "unknown"

with open("carbs_2.xml", "w") as fs:
    fs.write(file.toxml())

