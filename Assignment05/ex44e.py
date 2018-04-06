class Other(object):
    def override(self):
        print("OTHER override")
    def implicit(self):
        print("OTHER implicit()")
    def altered(self):
        print("OTHER altered()")

class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BIFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER altered()")

son = Child()
son.implicit()
son.override()
son.altered()
