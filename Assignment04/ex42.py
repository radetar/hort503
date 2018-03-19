## Animal is a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## dog is-a class and has-a  animal???
class Dog(Animal):
    def __init__(self, name):
        ##
        self.name = name
##cat is-a class ans has-a of animal objects
class Cat(Animal):

    def __init__(self, name):
        ##
        self.name = name
## Person is a class of objects
class Person(object):

    def __init__(self, name):
        ##
        self.name = name

        ##person has-a pet of some kind
        self.pet = None
##empployees are a class of people, which are a class of objects
class Employee(Person):

    def __init__(self, name, salary):
    ###hmm what is this strange magic
        super(Employee, self).__init__(name)
    ##
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

##rover is-a Dog
rover = Dog("Rover")

## satain is-a cat
satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

## frank is-a instance of class employee
frank = Employee("Frank", 120000)

##pet is an attribure of frank
frank.pet = rover

##
flipper = Fish()

crouse = Salmon()

harry = Halibut()
