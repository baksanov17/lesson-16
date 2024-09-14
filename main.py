def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])
vales_list = ['x', 32, False]
vales_dict = {'a': 'root', 'b': 45, 'c': 34.5}
print_params(*vales_list)
print_params(**vales_dict)
vales_list2 = ['privet', 777]
print_params(*vales_list2,42)

