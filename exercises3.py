# while True:
#     response = input('Give me input:')
#     if str(response).lower() == 'q':
#         break

# for n in range(1,20):
#     if n % 3 == 0:
#         continue
#     print(n)

print('\r\n')
def inputInt():
    try:
        response = int(input('Please input an integer: '))
        print(response)
        inputInt()
    except ValueError:
        print('You did not enter an integer.')
        inputInt()

inputInt()