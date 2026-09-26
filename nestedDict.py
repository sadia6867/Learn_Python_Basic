student = {
    "name": "John Doe",
    "subjects":{
        "phy": 95,
        "chem": 90,
        "math":95
    }
}
# print(student["subjects"]["chem"])
# print(list(student.keys()))
# print(len(student))
# print(list(student.values()))
# pairs = list(student.items())
student.update({"city":"New York"})
print(student)