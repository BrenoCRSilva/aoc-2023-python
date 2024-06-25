import sys
import re

def main():
    line = open(sys.argv[1]).read().strip().split("\n")
    add_dotted_line(line)
    matrix = [list(x) for x in line]
    add_dotted_column(matrix)
    row = len(matrix)
    column = len(matrix[0])
    print(p1(matrix, row, column))
 
def add_dotted_line(line):
    dot_line = "." * len(line)
    line.insert(0, dot_line)
    line.insert(len(line), dot_line) 

def add_dotted_column(matrix):
    for i in range(len(matrix)):
        matrix[i].insert(0, ".")
        matrix[i].insert(len(matrix[i]), ".")
    
def get_box(matrix, i, j):
    box = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            edge = matrix[i+x][j+y]
            box.append(edge)
    return box

def p1(matrix, row, column):
    check = False
    list_num = []
    n = "0"
    for i in range(1, row):
        for j in range(1, column):
            if j == 1:
                n = "0"
            if matrix[i][j].isdigit(): 
                box = get_box(matrix, i, j)
                box_string = "".join(box)
                special = re.findall(r"[^0-9.]", box_string)
                n += matrix[i][j]
                if len(special) != 0:
                    check = True
                        
                    
            elif not matrix[i][j].isdigit():
                if check == True:
                    list_num.append(int(n))
                    n = "0"
                    check = False
                else:
                    n = "0"

    return sum(list_num)

main()