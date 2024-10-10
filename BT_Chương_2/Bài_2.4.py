import xml.dom.minidom

# Tải và phân tích file XML
doc = xml.dom.minidom.parse("sample.xml")

# Lấy tất cả các phần tử
elements = doc.getElementsByTagName("*")

# In ra tên của từng phần tử
for element in elements:
    print("Element Name:", element.tagName)
