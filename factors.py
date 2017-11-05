response = input('Enter a positive integer:')

int_response = int(response)

for n in range(1, int_response):
    if int_response % n == 0:
        print(f'{n} is a divisor of {int_response}')