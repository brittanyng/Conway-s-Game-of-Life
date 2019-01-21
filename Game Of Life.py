"""
Author: Brittany Ng (bn798)
Course: CS1134 / Summer 2018

Homework 01: Conway's Game of Life
"""

import copy

def convert_file_to_matrix(file):
    """
    reads a text file and converts the format of given cells into matrix format
    """
    in_file = open(file)
    matrix = []
    for line in in_file:                   #separates each string in list and creates a row for each to add to matrix lst
        row = []
        for i in range(len(line)):
            if line[i] == "*":
                row.append(1)             #* represents alive cell
            else:
                row.append(0)             #- represents dead cell
        matrix.append(row)
    #print(matrix)
    in_file.close()
    return matrix

def create_matrix(rows, columns):
    """
    creates a matrix with the number of rows and columns specified when function is called
    """
    total_matrix = []
    for i in range(rows):
        mat_rows = [0] * columns
        total_matrix.append(mat_rows)
    return total_matrix

def add_border(matrix):
    """
    adds a column and a row of dead cells to surround existing matrix to allow easier
    implementation of the check_neighbor_life function
    """
    border_mat = []
    rows = len(matrix)
    column = len(matrix[0])
    horiz_border = [0] * (column + 2)          #top and bottom borders for matrix
    border_mat.append(horiz_border)

    for i in range(rows):
        row = [0]
        for k in range(column):
            row.append(matrix[i][k])
        row.append(0)
        border_mat.append(row)
    border_mat.append(horiz_border)
    return border_mat

def check_neighbor_life(matrix, x, y):          #x and y are the coordinates of the cell that is being checked for neighbors
    """
    takes a point in the matrix
    checks all points that are within 1 position away from point
    only counts the points that are alive
    """
    if matrix[x][y] == 1:
        neighbor_count = -1                     #starts at -1 because the loop takes in the point being checked as alive and will increment count by 1
    else:
        neighbor_count = 0

    for i in range(-1,2):
        for k in range(-1,2):
            if matrix[x+i][y+k] == 1:
                neighbor_count += 1
    return neighbor_count

def cell_life_and_death(matrix):
    """
    takes in a matrix and returns the next generation with updated cell life
    """
    unchanged_mat = copy.deepcopy(matrix)

    for i in range(1, len(matrix)-1):
        for k in range(1,len(matrix[i])-1):
            neighbor_life_count = check_neighbor_life(unchanged_mat, i, k)
            if neighbor_life_count == 3:
                matrix[i][k] = 1
            elif neighbor_life_count < 2 or neighbor_life_count > 3:
                matrix[i][k] = 0
    return matrix

def matrix_display(matrix):
    """
    provides a display of the matrix in current state
    """
    display = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                display += '*'
            else:
                display += '-'
        display += '\n'
    return display

def generations(gen_num, matrix):
    """
    creates the number of generations given and gives string output of each generation
    """
    final_display = ''
    for i in range(gen_num + 1):
        final_display += "Generation " + str(i) + ':\n'
        final_display += matrix_display(matrix)
        final_display += ("=" * 32) + '\n'

        matrix = add_border(matrix)
        #print(matrix)
        matrix = cell_life_and_death(matrix)
        #print(matrix)
        matrix.pop()                            #removes borders
        matrix.pop(0)
        for i in matrix:
            i.pop()
            i.pop(0)
    #print(final_display)
    return final_display

def main():
    gen_zero = convert_file_to_matrix('life.txt')
    matrix = create_matrix(10, 20)
    #print(matrix_world)
    for i in range(len(gen_zero)):
        for k in range(len(gen_zero[i])):
                matrix[i][k] = gen_zero[i][k]
    print(generations(10, matrix))

main()

#print(convert_file_to_matrix("life.txt"))
#create_matrix(10,10)

