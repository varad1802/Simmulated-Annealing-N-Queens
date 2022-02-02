import copy
from random import Random, randint, random
import numpy as np
import math
import decimal
import random


class Node:
    def __init__(self, board, hvalue) -> None:
        self.board = board
        self.hvalue = hvalue
    
    def printBoard(self):
        print(np.matrix(self.board))
    
class NQueen:
    def __init__(self, size, iterations) -> None:
        self.size = size
        self.iterations = iterations
        self.temperature = 4000
        self.sch = 0.99
    
    # Function to generate a random board position by placing one queen in each column
    def generateRandomPosition(self):
        numOfQueens = self.size
        mat = [['-' for i in range(numOfQueens)] for j in range(numOfQueens)]
        for y in range(numOfQueens): 
            queenPositionx = randint(0, self.size - 1)
            for x in range(numOfQueens):
                if (x == queenPositionx):
                    mat[x][y] = 'Q'
                else:
                    mat[x][y] = '-'
        return mat

    # Function to calculate the heuristic value of a given board position based on no of attacks
    def heuristicFunction(self, board):        
        heuristicValueRows = 0
        size = len(board)
        for x in board:
            count = x.count('Q')
            if(count > 1):
                heuristicValueRows = heuristicValueRows + (sum(range(x.count('Q'))))
        heuristicValueDiagonal = 0
        for y in range(size-1, -1, -1):
            numQueen = 0
            col = 0
            row = y
            while(col < size and row < size):
                value = board[row][col]
                if(value == 'Q'):
                    numQueen = numQueen + 1
                col = col + 1
                row = row + 1
            if(numQueen > 1):
                heuristicValueDiagonal = heuristicValueDiagonal + (sum(range(numQueen)))
        for y in range(size-1, 0, -1):
            numQueen = 0
            col = y
            row = 0
            while(col < size and row < size):
                value = board[row][col]
                if(value == 'Q'):
                    numQueen = numQueen + 1
                col = col + 1
                row = row + 1
            if(numQueen > 1):
                heuristicValueDiagonal = heuristicValueDiagonal + (sum(range(numQueen)))
        for y in range(size-1, -1, -1):
            numQueen = 0
            col = y
            row = 0
            while(col >= 0 and row < size):
                value = board[row][col]
                if(value == 'Q'):
                    numQueen = numQueen + 1
                col = col - 1
                row = row + 1
            if(numQueen > 1):
                heuristicValueDiagonal = heuristicValueDiagonal + (sum(range(numQueen)))
        for y in range(size-1, 0, -1):
            numQueen = 0
            col = size-1
            row = y
            while(col >= 0 and row < size):
                value = board[row][col]
                if(value == 'Q'):
                    numQueen = numQueen + 1
                col = col - 1
                row = row + 1
            if(numQueen > 1):
                heuristicValueDiagonal = heuristicValueDiagonal + (sum(range(numQueen)))
        heuristicValue = heuristicValueRows + heuristicValueDiagonal
        return heuristicValue

    def hillClimb(self):
        # Generate a random initial Board configuration
        board = NQueen.generateRandomPosition(self)
        current = Node(board, 0)
        print("Initial Board Configuration:")
        current.printBoard()
        current.hvalue = self.heuristicFunction(current.board)
        solution = False
        for count in range(0, self.iterations):
            # Decrease the temperature
            self.temperature = self.temperature * self.sch

            # Pick up a new random position and calculate its heuristic value
            tempBoard = NQueen.generateRandomPosition(self)
            tempHeuristic = self.heuristicFunction(tempBoard)
            tempNode = Node(tempBoard, tempHeuristic)
            difference = current.hvalue - tempNode.hvalue
            exponent = decimal.Decimal(decimal.Decimal(math.e) ** (decimal.Decimal(-difference) * decimal.Decimal(self.temperature)))

            # Move to the tempNode if the temp heuristic is better or is within the bounds of temperature(Based on Probability)
            if difference > 0 or random.uniform(0, 1) < exponent:
                current = tempNode

            # Solution Found
            if current.hvalue == 0:
                print("Solution found!")
                current.printBoard()
                solution = True
                break
        
        # Unsuccessful run
        if solution == False:
            print("The algorithm was unsuccessful in finding any solution!")


print("Enter number of Queens:")
noOfQueens = int(input())
print("Enter number of iterations:")
iterations = int(input())
nQueen = NQueen(noOfQueens, iterations)
nQueen.hillClimb()
