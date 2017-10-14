# using print() function w/out passing any arguments will print blank line

def invest(amount, rate, time):
    timeInt = int(time) + 1
    total = int(amount)
    percent = float(rate)
    print(f'principal amount: ${total}')
    print(f'annual rate of return: {percent}')
    for n in range(1,timeInt):
        total += (total * percent)
        print(f'year {n}: {total}')
    return total

invest(100, .05, 5)
# invest(2000, .025, 5)
