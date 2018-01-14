class A(object):
    def __init__(self):
        #眼睛
        self.eye = '眼睛'
    def sayHello(self):
        print('这是父亲的hello')
class C(object):
    def __init__(self):
        #脸
        self.face = '脸'
class D(C,A):
    def __init__(self):
        super(A,self).__init__()
    def sayHello(self):
        super().sayHello()
d = D()
print(d.eye)
print(d.face)


class B(A):
    def __init__(self):
        super().__init__()
        self.leg = '腿'
    def sayHello(self):
        print('这是儿子的hello')
        super().sayHello()

#b = B()
#b.sayHello()
#a = A()
#a.sayHello()
