import json

# Dữ liệu JSON
json_data = '''
{
    "company": {
        "name": "Công ty TNHH Đất Việt",
        "address": "abc Giải Phóng – Hà Nội",
        "employees": [
            {"unit": "Đơn vị A1", "name": "Nguyễn Văn A"},
            {"unit": "Đơn vị A2", "name": "Trần Thị B"},
            {"unit": "Đơn vị A1", "name": "Lê Văn C"},
            {"unit": "Đơn vị A3", "name": "Phạm Thị D"},
            {"unit": "Đơn vị A2", "name": "Ngô Văn E"}
        ]
    }
}
'''

# Chuyển đổi JSON thành đối tượng Python
data = json.loads(json_data)

# Thống kê nhân viên theo đơn vị
company_name = data["company"]["name"]
address = data["company"]["address"]
employees = data["company"]["employees"]

unit_stats = {}
for employee in employees:
    unit = employee["unit"]
    if unit not in unit_stats:
        unit_stats[unit] = 0
    unit_stats[unit] += 1

total_employees = len(employees)
print(f"Tên công ty: {company_name}")
print(f"Địa chỉ: {address}")
print("-----Thống kê nhân viên theo đơn vị------")
for unit, count in unit_stats.items():
    percentage = (count / total_employees) * 100
    print(f"Tên đơn vị: {unit} - Số nhân viên: {count} - Tỷ lệ: {percentage:.2f}%")
