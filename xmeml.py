import xml.etree.ElementTree as ET

class xmeml(xmlString):
    root = ET.fromstring(xmlString)
    
    def get_day():
        return root.find("./bin/name").text
