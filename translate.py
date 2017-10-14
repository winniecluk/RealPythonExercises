user_input = input('Enter some text: ')

new_str = user_input

leet_dict = {
    'a': '4',
    'b': '8',
    'e': '3',
    'l': '1',
    'o': '0',
    's': '5',
    't': '7'
}

# Python 2.x
# for key,value in leet_dict.iteritems():


for key,value in leet_dict.items():
    # print(key)
    # print(value)
    new_str = new_str.replace(key, value)
    # print(new_str)

print(new_str)
