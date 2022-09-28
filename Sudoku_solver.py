orginal = [
    [0,0,0, 0,0,0, 4,8,0],
    [0,5,0, 0,0,0, 0,0,3],
    [0,0,9, 2,5,0, 0,7,0],

    [0,0,0, 0,7,6, 0,1,0],
    [2,0,5, 0,4,0, 6,0,7],
    [0,8,0, 1,9,0, 0,0,0],
    
    [0,3,0, 0,8,5, 0,0,0],
    [4,0,0, 0,0,0, 0,6,0],
    [0,0,1, 4,0,0, 0,0,0],
]

sudoku = [
    [0,0,0, 0,0,0, 4,8,0],
    [0,5,0, 0,0,0, 0,0,3],
    [0,0,9, 2,5,0, 0,7,0],

    [0,0,0, 0,7,6, 0,1,0],
    [2,0,5, 0,4,0, 6,0,7],
    [0,8,0, 1,9,0, 0,0,0],
    
    [0,3,0, 0,8,5, 0,0,0],
    [4,0,0, 0,0,0, 0,6,0],
    [0,0,1, 4,0,0, 0,0,0],
]


def get_column(column : int) -> list:
    return [n[column] for n in sudoku]

def get_row(row : int) -> list:
    return sudoku[row]

def get_box(row : int, column : int) -> list:
    if row in range(3) and column in range(3):
        return [val for sublist in sudoku[:3] for val in sublist[:3]]
    if row in range(3) and column in range(3,6):
        return [val for sublist in sudoku[:3] for val in sublist[3:6]]
    if row in range(3) and column in range(6,9):
        return [val for sublist in sudoku[:3] for val in sublist[6:9]]

    if row in range(3,6) and column in range(3):
        return [val for sublist in sudoku[3:6] for val in sublist[:3]]
    if row in range(3,6) and column in range(3,6):
        return [val for sublist in sudoku[3:6] for val in sublist[3:6]]
    if row in range(3,6) and column in range(6,9):
        return [val for sublist in sudoku[3:6] for val in sublist[6:9]]

    if row in range(6,9) and column in range(3):
        return [val for sublist in sudoku[6:9] for val in sublist[:3]]
    if row in range(6,9) and column in range(3,6):
        return [val for sublist in sudoku[6:9] for val in sublist[3:6]]
    if row in range(6,9) and column in range(6,9):
        return [val for sublist in sudoku[6:9] for val in sublist[6:9]]

def print_sudoku_and_solution():
    print(f"Orginal: \t\t\t Solved:")
    for o_row, s_row in zip(orginal, sudoku):
        print(f"{o_row}\t{s_row}")

unsolved = True
numbers = set([n for n in range(0,10)])

while unsolved:
    # find least possiblities
    taken = 0
    values = {}
    pos_x = 0
    pos_y = 0
    
    for x in range(9):
        for y in range(9):
            n = sudoku[x][y]
            if n == 0: # its unasigned
                column = get_column(y)
                row = get_row(x)
                box = get_box(x, y)

                asigned_values = set(column + row + box)

                if (len(asigned_values) > taken):
                    values = asigned_values
                    taken = len(asigned_values)
                    pos_x = x
                    pos_y = y

    if (taken == 0 or taken == 10):
        unsolved = False
        break

    n = (numbers - values).pop()
    sudoku[pos_x][pos_y] = n


print_sudoku_and_solution()  





def test_get_box():
    for i in range(3):
        for j in range(3):
            result = get_box(i,j)
            assert result == [0, 0, 0, 0, 5, 0, 0, 0, 9], f"Should be [0, 0, 0, 0, 5, 0, 0, 0, 9], was {result}"
    
    for i in range(3):
        for j in range(3,6):
            result = get_box(i,j)
            assert result == [0, 0, 0, 0, 0, 0, 2, 5, 0], f"Should be [0, 0, 0, 0, 0, 0, 2, 5, 0], was {result}"

    for i in range(3):
        for j in range(6,9):
            result = get_box(i,j)
            assert result == [4, 8, 0, 0, 0, 3, 0, 7, 0], f"Should be [4, 8, 0, 0, 0, 3, 0, 7, 0], was {result}"

    for i in range(3,6):
        for j in range(3):
            result = get_box(i,j)
            assert result == [0, 0, 0, 2, 0, 5, 0, 8, 0], f"Should be [0, 0, 0, 2, 0, 5, 0, 8, 0], was {result}"

    for i in range(3,6):
        for j in range(3,6):
            result = get_box(i,j)
            assert result == [0, 7, 6, 0, 4, 0, 1, 9, 0], f"Should be [0, 7, 6, 0, 4, 0, 1, 9, 0], was {result}"

    for i in range(3,6):
        for j in range(6,9):
            result = get_box(i,j)
            assert result == [0, 1, 0, 6, 0, 7, 0, 0, 0], f"Should be [0, 1, 0, 6, 0, 7, 0, 0, 0], was {result}"

    for i in range(6,9):
        for j in range(3):
            result = get_box(i,j)
            assert result == [0, 3, 0, 4, 0, 0, 0, 0, 1], f"Should be [0, 3, 0, 4, 0, 0, 0, 0, 1], was {result}"

    for i in range(6,9):
        for j in range(3,6):
            result = get_box(i,j)
            assert result == [0, 8, 5, 0, 0, 0, 4, 0, 0], f"Should be [0, 8, 5, 0, 0, 0, 4, 0, 0], was {result}"

    for i in range(6,9):
        for j in range(6,9):
            result = get_box(i,j)
            assert result == [0, 0, 0, 0, 6, 0, 0, 0, 0], f"Should be [0, 0, 0, 0, 6, 0, 0, 0, 0], was {result}"

    return "Box Test : OK"

