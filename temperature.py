celsius_input = input('Enter degrees in Celsius: ')

def convert_to_f(c_num):
    fahrenheit = (c_num  * 9/5) + 32
    return fahrenheit

print(convert_to_f(37))

def convert_to_c(f_num):
    celsius = (f_num - 32) * 5/9
    return celsius

print(convert_to_c(72))

