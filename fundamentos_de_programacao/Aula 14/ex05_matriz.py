'''
add values in a matrix 2x4
print it in the screen
show value that is in second line and third column
'''

matrix = [[],[]]

for linha in range(2):
    for coluna in range(4):
        matrix[linha].append(int(input(f'Digite uma valor para a posição [{linha}] [{coluna}]: ')))
        print(matrix)

print()
print('*' * 24)
for linha in range(2):
        for coluna in range (4):
            print(f'[{matrix[linha][coluna]:^4}]', end="")
        
        print()

print('*' * 24)

print(f'\nlinha[0] coluna[2] da MATRIZ: [{matrix[0][2]:^4}]\n')
