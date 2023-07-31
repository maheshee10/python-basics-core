# one type of polymorphism -- no matter which class an object belong to if it has a method to work and is accesable thene it works
# def disp():
#     print('show display items')
#
#
# class A:
#     def execute(self):
#         print('execute the work given')
#
#     def add(self):
#         return 2 + 2
#
#     def show(self):
#         print('hai')
#
#
# class B:
#     def features(self,a):
#         a.execute()
#         print("B features")
#
# b = B()
# a = A()
# b.features(a)
class C:
    def ml(self):
        print("machine learning tools")


class D:
    def DeepLearn(self, object):
        object.ml()  # accesing a function of another class using object of this class

    def calling(self,obJ):
        return obJ


d = D()  # object d of D is created
c = C()
d.DeepLearn(c) # passing object of other class type as argument to D class using its d object

