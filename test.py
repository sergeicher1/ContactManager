class Person:
    def __init__(self, name):
        self.name = name  # name of the person (new object)

    def Name(self):
        return self.name

    def DisplayInfo(self):
        print(f"Name: {self.name}")


class Student(Person):
    # def __init__(self, name):
    #     self.name = name

    # def Name(self):
    #     return self.name
    #
    # def DisplayInfo(self):
    #     print(f"Name: {self.name}")
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def DisplayInfo(self):
        super().DisplayInfo()
        # print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

    def Learning(self):
        print(f"Name: {self.name} is learning")


person = Person("Tom")
person.DisplayInfo()

student = Student("Bob", "Java")
student.
# student.
# class Person:
#
#     def __init__(self, name):
#         self.__name = name
#         self.__age = 20
#
#     def DisplayInfo(self):
#         # print(f"Name: {self.name} Age: {self.age}")
#         pass
#
#     # Define attributes
#     def set_age(self, age):
#         if 1 < age < 110:
#             self.__age = age
#         else:
#             print("The age is not appropriate, please use number between 1 and 110")
#
#     def __get_age(self):
#         return self.__age
#
#     def _ShowInfo(self):
#         pass
#
#     def DisplayInfo(self, name):
#         print(f"Name = {self.__name} \t Age: {self.__age}")
#
#
# tom = Person("Tom")
# # print(tom.get_age())
# # tom.set_age(0)
# # tom.set_age(50)
# # print(tom.get_age())
# # print("Tom age: ", tom.age)
# # tom.age = -40
# # print("Tom age: ", tom.age)
#
# # int age = 0;
# # age = 20;
# #
# # int age = 20;
# tom.DisplayInfo()


# name = "Tom"
#
#
# def Hello():
#     name = "Sam"
#     print("Hello", name)
#
#
# def GoodBye():
#     print("Good bye", name)
#
#
# Hello()
# GoodBye()
