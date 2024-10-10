import xml.dom.minidom

# Tải và phân tích file XML
doc = xml.dom.minidom.parse("sample.xml")

# Lấy tên công ty
company_name = doc.getElementsByTagName("name")[0].childNodes[0].nodeValue
print("Company Name:", company_name)

# Lấy danh sách nhân viên
staffs = doc.getElementsByTagName("staff")

for staff in staffs:
    staff_id = staff.getAttribute("id")
    name = staff.getElementsByTagName("name")[0].firstChild.nodeValue
    salary = staff.getElementsByTagName("salary")[0].firstChild.nodeValue
    print(f"Staff ID: {staff_id}, Name: {name}, Salary: {salary}")