# multiple inheritence is possible
# MRO - method resolution orfder - Leftmethod given priority over right method...

# super() is used to call __init__() and other methods of its super classes
class A:
    def __init__(self):
        print("in A init")
    def feat1(self):
        print("features of A1")

    def feat2(self):
        print("features of A2")

class B:

    def __init__(self):
        print("in B init")
    def feat3(self):
        print("features of B1")

    def feat4(self):
            print("features of B2")

class C(A,B):

    def __init__(self):
        self.feat4()
        super().__init__()
        super().__init__()
    def feat5(self):
        print("in C")
        print(super().feat3())
        super().__init__()

objC = C()
objC.feat5()




