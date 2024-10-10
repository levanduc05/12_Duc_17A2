import json

# Đối tượng Python
python_obj = {"name": "John", "age": 30, "city": "New York"}

# Chuyển đổi đối tượng Python sang chuỗi JSON
json_str = json.dumps(python_obj)
print(json_str)

