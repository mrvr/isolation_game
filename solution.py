
class GameState:

    def __init__(self):
        from collections import namedtuple
        self.row_lim = 3
        self.col_lim = 2
        self.blocker = 1
        self.player1 = 2
        self.player2 = 3
        self.lastpos1 = [0,0]
        self.lastpos2 = [0,0]
        # TODO: Copy your implementation from the previous quiz
        coordinates = namedtuple("coordinates",['x','y'])
        location = namedtuple("location",['first','second'])
        self.board = [[0]*col_lim for _ in range(row_lim)]
        self.board[-1][-1] = blocker #block the last move
        self.initiator = 0 
        #location(first=coordinates(0,0),second=coordinates(0,0))
        self.currentlocation = [[0,0], [0,0]]
        
        # find if the board is empty
    def isEmpty():
        for i in self.row_lim:
            for j in self.col_lim:
                if (i,j)!=(2,1):
                    if self.board[i][j]!=0:
                        return FALSE
        return TRUE
                
                
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
        if isEmpty():
            return board
        
        moves = []
        loc = [0,0]
        if initiator==0:
            loc = self.lastpos1
        else
            loc = self.lastpos2
            
        #from current position move forward one step at a time
        # if the board  is not occupied, add the loc to moves
        #from current position move backworf till you encounter a hurdle
        # add all empty positions to moves
        #from current loc move diagonally forward till you encouter a black
        # add empty locations to moves
        #from current location move backword till you encounter a black
        # add all empty positions to the moves
                
                    
                
                    
                    

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
        pass
