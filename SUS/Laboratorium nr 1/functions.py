#Za argument podaje się dowolną ilość kolumn lub wierszy
def minmax(list, type="row"):
    column = lambda matrix, i: [row[i] for row in matrix]
    max_list = []
    found = {}

    if type=="row": size=len(list)
    elif type=="column": size=len(list[0])

    for i in range(size):
        if type=="row":
            max_list.append(max(list[i]))
        elif type=="column":
            max_list.append(max(column(list,i)))

    minimum = min(max_list)

    for key, el in enumerate(max_list):
        if el == minimum:
            found[key] = el

    return found

def maxmin(list, type="row"):
    column = lambda matrix, i: [row[i] for row in matrix]
    min_list = []
    found = {}

    if type=="row": size=len(list)
    elif type=="column": size=len(list[0])

    for i in range(size):
        if type=="row":
            min_list.append(min(list[i]))
        elif type=="column":
            min_list.append(min(column(list,i)))

    maximum = max(min_list)

    for key, el in enumerate(min_list):
        if el == maximum:
            found[key] = el

    return found