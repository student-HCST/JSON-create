import json
# Create data
student = {
    "name": "Rahul",
    "age": 20,
    "course": "B.Tech",
    "marks": 85
}

# Convert Python data into JSON string
json_data = json.dumps(student, indent=4)

print("JSON Data:")
print(json_data)

# Access data
print("\nStudent Details:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])