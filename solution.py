
class GameState:

    def __init__(self):
        from collections import namedtuple
        self.row_lim = 3
        self.col_lim = 2
        self.blocker = 1
        #self.player1 = 2
        #self.player2 = 3
        ######@index 0 gives first player location, Index 1 gives second player location
        self.player_loc=[None,None]
        self.lastpos1 = (0,0)
        self.lastpos2 = (0,0)
        # TODO: Copy your implementation from the previous quiz
        #coordinates = namedtuple("coordinates",['x','y'])
        #location = namedtuple("location",['first','second'])
        #self.board = [[0]* self.col_lim for _ in range(self.row_lim)]
        self.board = [[0]*self.col_lim for _ in range(self.row_lim)]
        self.board[-1][-1] = self.blocker #block the last move
        self.initiator = 0 
        #location(first=coordinates(0,0),second=coordinates(0,0))
        #self.currentlocation = [[0,0], [0,0]]
        
        # find if the board is empty
    def isEmpty(self):        
        row_lim = self.row_lim
        col_lim = self.col_lim
        for i in range (row_lim):
            for j in range (col_lim):
                if (i,j)!=(2,1):
                    if self.board[i][j]!=0:
                        return False
        return True
                
                
    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """
        # TODO: implement this function!
        from copy import deepcopy
        #check whether board initialized
        print("self.board = ",self.board)
        moves = []
        row_lim = self.row_lim
        col_lim = self.col_lim
        print("self.initiator ",self.initiator)
        loc = self.player_loc[self.initiator]
        print("Current ocation ",loc)
        
        if not loc:
            #board = deepcopy(self.board)
            #board[-1][-1]=1
            for col in range(0,col_lim):            
                for row in range(0,row_lim):
                    if self.board[row][col]!=1:
                        moves.append((col,row))
            return moves
        
        
        
            
#        if (loc[0] < 0 and loc[1] < 0) and (loc[0] >= self.row_lim and loc[1] >= self.col_lim):
#            return moves
        #from current position move forward one step at a time
        # if the board  is not occupied, add the loc to moves
        #from current position move backworf till you encounter a hurdle
        # add all empty positions to moves
        #from current loc move diagonally forward till you encouter a black
        # add empty locations to moves
        #from current location move backword till you encounter a black
        # add all empty positions to the moves
        #@@@ backward moves    
        
        row = loc[0] #move a step back by row wise
        col = loc[1]
        while col >= 0:            
            while (row >= 0):
                if (self.board[row][col]!=0):                    
                    break;
                #if (row,col) not in moves:
                if (col,row) not in moves:
                    moves.append((col,row))
                row-=1                
            col-=1
        
#        for i in range (loc[0],0,-1):
#            ''' backward moves'''
#            for j in range(loc[1]-1,0,-1):
#                if ((j < 0) and (self.board[i][j]!=0) ):
#                    break                
#                #if [i,j] not in moves:
#                if [j,i] not in moves:
#                        #moves.append((i,j))
#                        moves.append((j,i))
        for j in range(loc[1],self.col_lim):    
            "forward moves"
            for i in range (loc[0],self.row_lim):
                if ((j>=self.col_lim) and (self.board[i][j]!=0)) :
                    break
                else:
                    #if [i,j] not in moves:
                    if (j,i) not in moves:
                        #moves.append((i,j))
                        moves.append((j,i))
                                    
        #column wise forward moves
        for j in range(loc[1],self.col_lim):        
            "column wise forward moves"
            for i in range (loc[0],self.row_lim):
                if ((j>=self.col_lim) and (self.board[j][i]!=0)):
                    break
                else:
                    #if [i,j] not in moves:
                    if (j,i) not in moves:
                        #moves.append((i,j))           
                        moves.append((j,i))
        
        #Column wise backward moves
        for j in range(loc[1],0,-1):        
            ''' column wise backward moves'''
            for i in range (loc[0],0,-1):
                if ( (j < 0) and (self.board[j][i]!=0)):
                    break
                else:
                    #if [i,j] not in moves:
                    if (j,i) not in moves:
                        #moves.append((i,j))
                        moves.append((j,i))
                
        #diagonal forward moves
        i,j = loc[0],loc[1]
        while((j < self.col_lim) and (i < self.row_lim) ):
           "column wise forward moves"            
           if self.board[i][j]!=0:
               break
           #if [i,j] not in moves:
           if (j,i) not in moves:
                moves.append((j,i))
           i+=1
           j+=1
        
        #diagonal forward moves
        i,j = loc[0],loc[1]
        while((i >= 0) and (j >= 0)):
            "column wise forward moves"            
            if self.board[i][j]!=0:
                break
            #if [i,j] not in moves:
            if [j,i] not in moves:
                moves.append((j,i))
            i-=1
            j-=1
            
        return moves
    
    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.
        
        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
            (e.g., (0, 0) if the active player will move to the
            top-left corner of the board)
        """
        # TODO: implement this function!
        from copy import deepcopy
        #check if the move is legal
        print("move",move)
        legal_moves = self.get_legal_moves()
        print("legal_moves =",legal_moves)
        if move not in legal_moves:
        #if (([move[0],move[1]] not in legal_moves) or (move not in legal_moves)):
        #if move not in self.get_legal_moves():
            raise RuntimeError("Illegal move")
        
        #self.initiator ^= 1
        #self.player_loc[self.initiator]=move
        #create a new board
        nboard = deepcopy(self)
        #block the last box
        nboard.board[move[0]][move[1]] = 1
        nboard.player_loc[nboard.initiator]=move
        nboard.initiator ^=1
        
        
#        if self.initiator == 0:
#            #self.board[move[0]][move[1]] = 2
#            self.initiator = 1
#        else:
#            #self.board[move[0]][move[1]] = 3
#            self.initiator = 0
        
        return nboard