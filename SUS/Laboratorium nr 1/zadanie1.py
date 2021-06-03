from functions import *

matrix = [[1, 3, 4, -2], 
          [-4, -1, 2, 1], 
          [-2, 5, 0, -3], 
          [8, -6, -3, 5]]


strategy = 2
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
print(second_player)
print('--------------------')

fir_iter = iter(first_player)
sec_iter = iter(second_player)

#Wybieramy pierwszy element z każdej listy, 
#praktycznie może to być dowolny element,
#z poziomu bezpieczeństwa
if next(fir_iter) == next(sec_iter):
    print("Odnaleziono punkt siodłowy")

id_1 = list(first_player.keys())[0]
id_2 = list(second_player.keys())[0]

value = matrix[id_1][id_2]

if value > 0:
    print('Gracz nr 2 wygrywa, gracz nr 1 przegrywa')
elif value < 0:
    print('Gracz nr 1 wygrywa, gracz nr 2 przegrywa')
else:
    print('remis')

print('wybrana wartość: ' + str(value))

