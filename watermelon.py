try:
    weight = int(input())

    while not (1 <= weight <= 100):
        weight = int(input())       
    if weight == 2:
        print('No')
    elif weight % 2 == 0:
        print('YES')
    else:
        print('NO')
except ValueError as e:
    print(f'Error: {e}')