import json

# Đối tượng từ điển Python
python_dict = {"name": "John", "age": 30, "city": "New York"}

# Chuyển đổi đối tượng từ điển Python thành dữ liệu JSON
json_str = json.dumps(python_dict, indent=4, sort_keys=True)
print(json_str)
