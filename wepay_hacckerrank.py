class Sample:
    def __init__(self):
        self.a = 1;
        self.b = 1;

    def function_one(self, a):
        self.b = self.b + a;
        print(self.a)
        print(self.b)

    def function_two(self, b):
        for i in range(self.b):
            self.a += b

    def print(self):
        print(str(self.a) + ", " + str(self.b))
"""
What values of x, y, and z are needed to print "25, 6"?
"""
s = Sample()

s.function_one(1)
s.function_two(12)
s.function_one(4)
s.print()
