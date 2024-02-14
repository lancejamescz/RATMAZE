import numpy as np

N = int(input('Input maze height:'))
M = int(input('Input maze width:'))


def printSolution( sol ): 
    for i in sol: 
        for j in i: 
            print(str(j) + " ", end ="") 
        print("") 


def canMove( maze, x, y ): 
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1: 
        return True     
    return False

def mazeSolver( maze ): 
    sol = [ [ 0 for j in range(4) ] for i in range(4) ] 
    if mazeSolverUtil(maze, 0, 0, sol) == False: 
        print("Solution doesn't exist"); 
        return False     
    printSolution(sol) 
    return True
      
def mazeSolverUtil(maze, x, y, sol): 
    if x == N - 1 and y == N - 1: 
        sol[x][y] = 1
        return True
    if canMove(maze, x, y) == True:   
        sol[x][y] = 1         
        if mazeSolverUtil(maze, x + 1, y, sol) == True: 
            return True             
        if mazeSolverUtil(maze, x, y + 1, sol) == True: 
            return True
        sol[x][y] = 0
        return False
  
 
if __name__ == "__main__": 
    A = np.random.randint(2, size=(N,M))
    
    mazeSolver(A) 
    print(printSolution)



    
