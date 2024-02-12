# # object oriented programming
# # class name should start in caps
# class Person:
#     def __init__(self):
#         self.name = "jay"
#         self.age = 19
#         self.location = "nairobi"
#         self.gender = "male"
#
# oopp = Person()
# oopp.name = "Spencer"
# print(oopp.name)
# print(oopp.age)
# print(oopp.gender)
# print(oopp.location)

class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


person1 = People("jay",19,"male")
person2 = People("spence",21,"male")

print(person1.name)
print( f"my name is {person1.name} and im {person1.age} years and im a {person1.gender}" )
