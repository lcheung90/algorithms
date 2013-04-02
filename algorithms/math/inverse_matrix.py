"""
	inverse_matrix.py

	Recursive implementation to calculate the inverse of a square matrix.

	Matrix Inversion:
	--------------------------
	AB = BA = I

	Matrix inversion is the process of finding the matrix B that satisfies
	the previous equation for a given invertable matrix A

"""

from copy import deepcopy

def checkMatrix(matrix):
    order = len(matrix)
    if order == 1:
        return False
    else:
        for i in xrange(len(matrix)):
            if type(matrix[i]) == int or type(matrix[i]) == float:
                return False
            else:
                if order != len(matrix[i]):
                   return False
                else:
                   return True

def trim(matrix,row,col):
    matrix = list(matrix)
    temp = deepcopy(matrix)
    temp.pop(row)
    for r in temp:
        del r[col]
    return tuple(temp)

def findDet(matrix):
    order = len(matrix)
    pdets = []
    det = 0
    if order == 1:
        return matrix[0][0]
    elif order == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    else:
        for col in xrange(order):
            smatrix = trim(matrix,0,col)
            pdet = matrix[0][col]*findDet(smatrix)
            pdets.append(pdet)
        for index in xrange(len(pdets)):
            det += pow(-1, index % 2) * pdets[index]  
        return det

def computeMinMatrix(matrix):
    minorMatrix = []
    temp = deepcopy(matrix)
    order = len(temp)
    for row in xrange(order):
        mrow = []
        for col in xrange(order):
            minor = trim(temp,row,col)
            element = findDet(minor)
            mrow.append(element)
        minorMatrix.append(mrow)
    return tuple(minorMatrix)

def computeCofMatrix(matrix):
    cofactorMatrix = []
    order = len(matrix)
    cofactorMatrix = ([matrix[row][col]*pow(-1,row+col) for col in xrange(order)] for row in xrange(order))
    return tuple(cofactorMatrix)

def transpose(matrix):
    cmatrix = list(matrix)
    order = len(matrix)
    for i in xrange(order):
        for j in xrange(i): 
            cmatrix[j][i], cmatrix[i][j] = cmatrix[i][j], cmatrix[j][i]                 
    return tuple(cmatrix)

def inverseMatrixHelper(matrix,determinant):
    order = len(matrix)
    inverse = [[matrix[row][col]/float(determinant) for col in xrange(order)] for row in xrange(order)]
    return tuple(inverse)

def inverseMatrix(matrix):
    if checkMatrix(matrix):
        determinant = findDet(matrix)
        minorMatrix = computeMinMatrix(matrix)
        cofactorMatrix = computeCofMatrix(minorMatrix)
        transposeMatrix = transpose(cofactorMatrix)
        inverseMatrix = inverseMatrixHelper(transposeMatrix,determinant)
        return inverseMatrix
    else:
        return "Matrix is not square"
