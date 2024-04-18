def print_params(a=1, b='str', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])


def print_params(*params):
    print(*params)


print_params(1, 2, 3, 4, 5, 6, 7, 8)


def print_params():
    print('hello')


print_params()


def print_params(a, b, c):
    print(a, b, c)
values_list = (1, 'hi', 1.1)
values_dict = {2, 'bye', 2.2}
print_params(*values_list)
print_params(*values_dict)
value_list2 = (3.3, 'damn')
print_params(*value_list2, 42)