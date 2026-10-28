# Configuration setting example
class Config:
    course_name = "Python Basics"

c1 = Config()
c2 = Config()
print("c1:", c1.course_name)
print("c2:", c2.course_name)
Config.course_name = "Advanced Python"
print("After update c1:", c1.course_name)
print("After update c2:", c2.course_name)
c1.course_name = "Instance override"
print("c1:", c1.course_name, "| c2:", c2.course_name, "| class:", Config.course_name)
