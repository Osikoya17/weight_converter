weight = int(input('Weight: '))
measure = input('(L)bs or (K)g: ')
if measure.upper() == 'L':
    kilo = int(weight) * 0.45
    print(f'your weight is {kilo} kilos')
elif measure.upper() == 'K`':
    pounds = int(weight) / 0.45
    print(f'your weight is {pounds} lbs')
else:
    print('invalid')

