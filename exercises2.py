# def square(number):
#     sqr_num = number * number
#     return sqr_num

# def add_two_numbers(num1, num2):
#     sum = num1 + num2
#     return sum

# def cube(num):
#     return num ** 3

# print(cube(3))


# def multiply(num1, num2):
#     return num1 * num2

# print(multiply(2,5))

''' while loop '''
# n = 1
# while (n < 5):
#     print('n =', n)
#     n = n + 1
# print('loop finished')

# for n in range(1, 5):
#     print('n =', n)

# print('loop finished')


# for n in range(1,4):
#     for j in ['a', 'b', 'c']:
#         print('n = {}'.format(n), 'and j = {}'.format(j))

# for n in range(2,11):
#     print(n)

# n = 2
# while n < 11:
#     print(n)
#     n += 1

# def doubles(num):
#     for n in range(1,4):
#         num = num * 2
#         print(num)
#     return num

# print(doubles(2))

# print(1 <= 1)
# #True
# print(1 != 1)
# #False
# print(1 != 2)
# #True
# print('good' != 'bad')
# #True
# print('good' != 'Good')
# #True
# print(123 == '123')
# #False


# def cube(num):
#     return num **c


def input(word):
    stored_word = str(word)
    if len(stored_word) < 5:
        print('word is less than 5 letters')
    elif len(stored_word) == 5:
        print('word has 5 letters')
    else:
        print('word has more than 5 letters')

input('turkey')
