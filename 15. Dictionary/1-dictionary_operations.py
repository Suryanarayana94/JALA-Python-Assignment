# Dictionary: student IDs to names with add/update/access/iterate/delete/nested
students = {101: "Alice", 102: "Bob", 103: "Charlie", 104: "David", 105: "Eve"}
# 1.1 Add
students[106] = "Frank"
# 1.2 Update
students[101] = "Alice Updated"
# 1.3 Access
print("101:", students[101])
print("All names:", list(students.values()))
# 1.4 Iterate
for k, v in students.items():
    print(k, v)
# 1.5 Keys
print("Keys:", list(students.keys()))
# 1.6 Values
print("Values:", list(students.values()))
# 1.7 Nested
nested = {101: {"name": "abc", "age": 22}, 102: {"name": "xyz", "age": 21}}
# 1.8 Access nested
print("101 name:", nested[101]["name"], "age:", nested[101]["age"])
# 1.9 Delete
del students[106]
print("After del:", students)
last = students.popitem()
print("popitem removed:", last)
removed = students.pop(102)
print("pop 102:", removed)
print("Final:", students)
