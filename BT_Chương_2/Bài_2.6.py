import json

# Dữ liệu JSON
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Chuyển đổi JSON thành đối tượng Python
python_obj = json.loads(json_data)
print(python_obj)
