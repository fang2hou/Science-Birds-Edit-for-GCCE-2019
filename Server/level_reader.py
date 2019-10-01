import xml.etree.ElementTree as ET
root = ET.parse('new.xml').getroot()
blocks = root.find('GameObjects').iter()
a = 0
for block in blocks:
    if a != 0:
        print(block.tag)
        print(block.get("material"))
        print(block.get("x"))
    a += 1