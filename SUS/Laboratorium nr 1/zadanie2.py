from functions import *

matrix = [[1, -4, 5, -2, 0, -2], 
          [-4, -1, 2, 1, -1, 3], 
          [-2, -5, 0, -3, 1, 9], 
          [8, -2, -1, 5, -2, -1], 
          [1, 2, -2, 4, -5, -6], 
          [7, 5, -1, 1, -4, -6]]

strategy = 1
if strategy == 1:
    first_player = minmax(matrix, "row")
    second_player = maxmin(matrix, "column")
elif strategy == 2:
    first_player = maxmin(matrix, "row")
    second_player = minmax(matrix, 'column')


print("STRATEGIE BEZPIECZNE")
print("Wyniki podane są w słowniku. Klucz oznacza numer wiersza lub kolumny")

print('--------------------')
print("gracz nr 1 - wiersze")
print(first_player)

print("gracz nr 2 - kolumny")
print('--------------------')
print(second_player)

fir_iter = iter(first_player)
sec_iter = iter(second_player)

if next(fir_iter) == next(sec_iter):
    print("Odnaleziono punkt siodłowy")

level = 1
print('')
print('Poziom gry = ' + str(level))
if level == 1:
    id_1 = list(first_player.keys())[0]
    id_2 = list(second_player.keys())[0]
elif level == 2:
    id_1 = list(first_player.keys())[0]
    id_2 = list(second_player.keys())[1]
elif level == 3:
    id_1 = list(first_player.keys())[1]
    id_2 = list(second_player.keys())[0]
elif level == 4:
    id_1 = list(first_player.keys())[1]
    id_2 = list(second_player.keys())[1]

value = matrix[id_1][id_2]
print('Wybrano wiersz: ' + str(id_1) + ' oraz kolumnę: ' + str(id_2))
if value > 0:
    print('Gracz nr 2 wygrywa, gracz nr 1 przegrywa')
elif value < 0:
    print('Gracz nr 1 wygrywa, gracz nr 2 przegrywa')
else:
    print('remis')

print('wybrana wartość: ' + str(value))

