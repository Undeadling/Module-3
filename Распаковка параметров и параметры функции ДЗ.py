def print_params(a=1, b='str', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c = [1,2,3])

def print_params(*params):
    print(*params)


print_params(1, 2, 3, 4, 5, 6, 7, 8)


def print_params():
    print('hello')


print_params()
