#Syntax:
'''class derived-class(base class):
    <class-suite>

class derive-class(<base class 1>, <base class 2>, ..... <base class n>):
    <class - suite>
'''

#Inharitence of class
# class Calculation1:
#     def Summation(self,a,b):
#         return a+b;
# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b;
# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b;
# d = Derived()
# print(d.Summation(10,20))
# print(d.Multiplication(10,20))
# print(d.Divide(10,20))

###issubclass method
# class Calculation1:
#     def Summation(self,a,b):
#         return a+b;
# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b;
# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b;
# d = Derived()
# print(issubclass(Derived,Calculation2))
# print(issubclass(Calculation1,Calculation2))


##isinstance method
# class Calculation1:
#     def Summation(self,a,b):
#         return a+b;
# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b;
# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b;
# d = Derived()
# print(isinstance(d,Derived))


#Method Overidding
# class Animal:
#     def speak(self):
#         print("speaking")
# class Dog(Animal):
#     def speak(self):
#         #super().speak()
#         #Animal.speak(self)
#         print("Barking")
# d = Dog()
# d.speak()


# Method Overloading
# # First product method.
# # Takes two argument and print their
# # product
def product(a, b):
    p = a * b
    print(p)


# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b * c
    print(p)


# Uncommenting the below line shows an error
#product(4, 5)

# This line will call the second product method
# product(4, 5, 5)



# play with private and Protect and Public access modifier in a class
# super class
# class Student:
#
#      # protected data members
#      _name = None
#      _roll = None
#      _branch = None
#
#      # constructor
#      def __init__(self, name, roll, branch):
#           self._name = name
#           self._roll = roll
#           self._branch = branch
#
#      # protected member function
#      def _displayRollAndBranch(self):
#
#           # accessing protected data members
#           print("Company ID: ", self._roll)
#           print("Company: ", self._branch)
#
#
# # derived class
# class Geek(Student):
#
#        # constructor
#        def __init__(self, name, roll, branch):
#                 Student.__init__(self, name, roll, branch)
#
#        # public member function
#        def displayDetails(self):
#
#                  # accessing protected data members of super class
#                 print("Name: ", self._name)
#
#                  # accessing protected member functions of super class
#                 self._displayRollAndBranch()
#
# # creating objects of the derived class
# obj = Geek("KG", 1706256, "Kohler")
#
# # calling public member functions of the class
# obj.displayDetails()

## public and protect and private data member and function
# super class
# class Super:
#     # public data member
#     var1 = None
#     # protected data member
#     _var2 = None
#     # private data member
#     __var3 = None
#     # constructor
#     def __init__(self, var1, var2, var3):
#         self.var1 = var1
#         self._var2 = var2
#         self.__var3 = var3
#
#     # public member function
#     def displayPublicMembers(self):
#         # accessing public data members
#         print("Public Data Member: ", self.var1)
#
#     # protected member function
#     def _displayProtectedMembers(self):
#         # accessing protected data members
#         print("Protected Data Member: ", self._var2)
#
#     # private member function
#     def __displayPrivateMembers(self):
#         # accessing private data members
#         print("Private Data Member: ", self.__var3)
#
#     # public member function
#     def accessPrivateMembers(self):
#         # accessing private member function
#         self.__displayPrivateMembers()
#
#
# # derived class
# class Sub(Super):
#
#     # constructor
#     def __init__(self, var1, var2, var3):
#         Super.__init__(self, var1, var2, var3)
#
#     # public member function
#     def accessProtectedMembers(self):
#         # accessing protected member functions of super class
#         self._displayProtectedMembers()
#
#
# # creating objects of the derived class
# obj = Sub("Kohler", "Bold", "Pune")
#
# # calling public member functions of the class
# obj.displayPublicMembers()
# obj.accessProtectedMembers()
# obj.accessPrivateMembers()
#
# # Object can access protected member
# print("Object is accessing protected member:", obj._var2)
#
# # Object can access private member
# #print("Object is accessing protected member:", obj.__var2)

