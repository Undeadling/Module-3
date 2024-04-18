#1й вариант
def test():
    a = 1
    b = 2
    print(a, b)
    print(a)
    print(b)
test()

def test2():
    a = 1
    b = 2
    c = 3
    print(a, b, c)
    print(a)
    print(b)
    print(c)
test2()

#2й вариант

def test3(a = 1, b = 2):
    print(a, b)
    print(a)
    print(b)
    print(a + b)
test3(3, 4)

def test4(a = 1, b = 2, c = 3):
    print(a, b, c)
    print(a)
    print(b)
    print(c)
    print(a + b + c)
test4(4, 5, 6)

