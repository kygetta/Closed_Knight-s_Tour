#Authors: Mathias Boddicker, Kylie Hall, Liam Zalubas, Caleb Jenkins
import sys

class DFSsolver():

    def __init__(self, n, startnode):
        self.board = [[-1 for i in range(n)]for i in range(n)]
        self.boardsize = n
        self.startnode = startnode
        self.move_x = [2, 1, -1, -2, -2, -1, 1, 2]
        self.move_y = [1, 2, 2, 1, -1, -2, -2, -1]
        self.solutions = []
        self.solutionfound = True

    def dfs(self, x, y, pos):
        #Checks if closed tour, appends board, and returns
        if(pos == self.boardsize*self.boardsize and [y,x] == self.startnode):
            self.solutions.append(self.board)
            return
            """self.solutionfound = False"""
        #Checks if open tour and returns
        elif(pos == self.boardsize*self.boardsize and [y,x] != self.startnode):
            return
        #Adds new move to board
        self.board[y][x] = pos

        #checks possible moves and recurses through solutions
        for i in range(8):
            new_x = x+self.move_x[i]
            new_y = y+self.move_y[i]
            if(self.isSafe(new_x, new_y)):
                self.dfs(new_x,new_y,pos+1)
        #reverts board position when recursing out
        self.board[y][x] = -1
        return

            
    

    """def solve(self, x, y, pos):
        self.board[0][0] = 0
        self.printboard
        print()
        if(not self.solver(0, 0, 0)):
            print("Solution does not exist")
        else:
            self.printboard()"""

    """ def solver(self, x, y, pos):
        if(pos == self.boardsize*self.boardsize):
            return True
        
        for i in range(self.boardsize):
            new_x = x + self.move_x[i]
            new_y = y + self.move_y[i]
            if(self.isSafe(new_x, new_y)):
                self.board[new_y][new_x] = pos
                self.board[0][0] = 0
                self.printboard
                if(self.solver(new_x, new_y, pos+1)):
                    return True

                self.board[new_y][new_x] = -1
        return False """
            
        
    #Given x,y coords and the board, checks to see if space is open and possible
    def isSafe(self, x, y):
        if(x >= 0 and y >= 0 and x < self.boardsize and y < self.boardsize and self.board[y][x] == -1):
            return True
        return False
    
    #prints board
    def printboard(self):
        for row in self.board:
            print(row)


if __name__ == "__main__":

    """parses first 3 args for board size, x, and y"""
    n = sys.argv[1]
    x = sys.argv[2]
    y = sys.argv[3]
    s = DFSsolver(n, [y,x])
    s.dfs(x,y,0)

    """Outputs solutions, if any, to text file"""
    with open('output.txt', 'a') as f:
        if(s.solutions == []):
            print("no solution")
        else:
            for i in range(s.solutions): 
                for j in range(s.solutions[i]):
                    f.write(s.solutions[i][j])

    
