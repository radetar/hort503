class Parent(object):
    def altered(self):
        print("Parent altered()")

class Child(Parent):
    def altered(self):
        print("CHILD, before parent altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PAREN altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()
