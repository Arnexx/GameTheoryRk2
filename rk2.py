import numpy as np
from numpy.linalg import inv
from numpy.linalg import det
from pprint import pprint

A = [[ 10, 0],
     [2, 9]]

B = [[ 7, 4],
      [1, 3]]

def printStrategies(X, Y):
    print('strategy A: {} strategy B: {}' .format(X, Y))

def checkIfCase1(A, B):
    aStrategy = [0, 0]
    bStrategy = [0, 0]
    if A[0][0] > A[1][0] and A[0][1] > A[1][1]:
        aStrategy = [1, 0]
        bStrategy = [1, 0] if B[0][0] > B[0][1] else [0, 1]
        print('case 1!')
		print('Matrix A:')
        print(A[0])
        print(A[1])
        print('Matrix B:')
        print(B[0])
        print(B[1])
        printStrategies(aStrategy, bStrategy)
        return True

    if A[1][0] > A[0][0] and A[1][1] > A[0][1]:
        aStrategy = [0, 1]
        bStrategy = [1, 0] if B[1][0] > B[1][1] else [0, 1]
        print('case 1!')
		print('Matrix A:')
        print(A[0])
        print(A[1])
        print('Matrix B:')
        print(B[0])
        print(B[1])
        printStrategies(aStrategy, bStrategy)
        return True

    if B[0][0] > B[0][1] and B[1][0] > B[1][1]:
        bStrategy = [1, 0]
        aStrategy = [1, 0] if A[0][0] > A[1][0] else [0, 1]
        print('case 1!')
		print('Matrix A:')
        print(A[0])
        print(A[1])
        print('Matrix B:')
        print(B[0])
        print(B[1])
        printStrategies(aStrategy, bStrategy)
        return True

    if B[0][1] > B[0][0] and B[1][1] > B[1][0]:
        bStrategy = [0, 1]
        aStrategy = [1, 0] if A[0][1] > A[1][1] else [0, 1]
        print('case 1!')
		print('Matrix A:')
        print(A[0])
        print(A[1])
        print('Matrix B:')
        print(B[0])
        print(B[1])
        printStrategies(aStrategy, bStrategy)
        return True

    return False

def getMixedStrategies(A, B):

    if det(A) and det(B):
        AInv, BInv = inv(A), inv(B)
        u = np.ones(2)
        v1 = 1 / (u @ AInv @ u)
        v2 = 1 / (u @ BInv @ u)
        aStrategy = (u @ BInv) * v2
        bStrategy = (AInv @ u) * v1
    return (aStrategy, bStrategy)

def checkIfCase2(A, B):
    if (A[1][0] < A[0][0] and A[0][1] < A[1][1] and B[0][0] < B[0][1] and B[1][1] < B[1][0]) or (A[0][0] < A[1][0] and A[1][1] < A[0][1] and B[0][1] < B[0][0] and B[1][0] < B[1][1]):

        aStrategy, bStrategy = getMixedStrategies(A, B)
        print('case 2!')
		print('Matrix A:')
        print(A[0])
        print(A[1])
        print('Matrix B:')
        print(B[0])
        print(B[1])
        printStrategies(aStrategy, bStrategy)
        return True
    return False

def checkIfCase3(A, B):

    if A[1][0] < A[0][0] and A[0][1] < A[1][1] and B[0][1] < B[0][0] and B[1][0] < B[1][1]:
	    print('case 3!')
        print('Matrix A:')
        print(A[0])
        print(A[1])
        print('Matrix B:')
        print(B[0])
        print(B[1])
        print('\nNash:');
        print('{ [', A[0][0], ',', B[0][0],'], [', A[1][1], ',', B[1][1], '] }')
        aStrategy, bStrategy = getMixedStrategies(A, B)
        printStrategies(aStrategy, bStrategy)
        return True

    if A[0][0] < A[1][0] and A[1][1] < A[0][1] and B[0][0] < B[1][1] and B[0][1] < B[1][0]:
	    print('case 3!')
        print('Matrix A:')
        print(A[0])
        print(A[1])
        print('Matrix B:')
        print(B[0])
        print(B[1])
        print('\nNash:');
        print('{ [', A[0][1], ',', B[0][1],'], [', A[1][0], ',', B[1][0], '] }')
        aStrategy, bStrategy = getMixedStrategies(A, B)
        printStrategies(aStrategy, bStrategy)
        return True
    return False

def findGamePrice(A, B):
    if det(A) and det(B):
        AInv, BInv = inv(A), inv(B)
        u = np.ones(2)
        v1 = 1 / (u @ AInv @ u)
        v2 = 1 / (u @ BInv @ u)
        print('v1 = %s' % v1)
        print('v2 = %s' % v2)

       


if not checkIfCase1(A, B):
    if not checkIfCase2(A, B):
        checkIfCase3(A, B)
findGamePrice(A, B)
