class A:
    vc = 123

a1 = A()
a2 = A()

A.vc = 312


print(a1.vc)