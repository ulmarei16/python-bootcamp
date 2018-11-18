a = 1

def foo():
    a = 0
    print(a)

def foo2():
    print(a)

def foo3():
    b = 2
    print(locals())
    print(globals())

foo()
foo2()
print(a)