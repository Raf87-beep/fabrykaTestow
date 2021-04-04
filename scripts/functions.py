# def function():
#     print('my first function')
#
# function()

# def function_new(name, language):
#     print('Hello ' + name + ' it is your first ' + language + ' function')
#
# function_new('Paul', 'Python')

# def divide(divident, divisor):
#     if(divisor == 0):
#         return False
#     else:
#         return divident / divisor
# print(divide(5,0))
# print(divide(10,2))

# def my_function(arg1, arg2 = 'Alfa Romeo'):
#     return f'{arg1} {arg2}'
#
# print(my_function(arg1='car', arg2='Fiat'))

from functools import partial

def division(x,y):
    return x/y

divide_by_two = partial(division,2)

print(divide_by_two(6))
print(divide_by_two(11))
print(divide_by_two(7))