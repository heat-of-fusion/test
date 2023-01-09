for i in range(1, 10):
    print('*'*i, ' '*i, '*'*i, ' '*i, '*'*i)

for i in range(1, 10):
    print(' '*(9-i), ' '*(9-i), ' '*(9-i), ' '*(9-i), ' '*(9-i), end='')
    print('*'*i, ' '*i, '*'*i, ' '*i, '*'*i, end='')
    print(' '*i, '*'*i, ' '*i, '*'*i, ' '*i, '*'*i)