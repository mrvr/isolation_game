#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:20:53 2018

@author: raghuvardhan
"""
from copy import deepcopy

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
        self.initiator = 0 #curren player
        #location(first=coordinates(0,0),second=coordinates(0,0))
        #self.currentlocation = [[0,0], [0,0]]
        
        # find if the board is empty
    def isEmpty(self):        
        row_lim = self.row_lim
        col_lim = self.col_lim
        for i in range (row_lim):
            for j in range (col_lim):
                if (i,j)!=(row_lim-1,col_lim-1):
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
        
        #check whether board initialized
        print("self.board = ",self.board)
        moves = []
        row_lim = self.row_lim
        col_lim = self.col_lim
        print("self.initiator ",self.initiator)
        loc = self.player_loc[self.initiator]
        print("Current location ",loc)
        
        if loc is None:
            #board = deepcopy(self.board)
            #board[-1][-1]=1            
            for col in range(col_lim):            
                for row in range(row_lim):
                    if self.board[row][col]!=1:
                        #moves.append((col,row))
                        moves.append((row,col))
            print("Initial moves ",moves)
            return list(set(moves))
        
        
        
            
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
        
        row = loc[0] 
        col = loc[1]+1
        #forward moves on row wise                    
        while col < self.col_lim:
            if (self.board[row][col]!=0):                         
                break;
            #if (row,col) not in moves:
            #moves.append((col,row))
            moves.append((row,col))
            col+=1              
        
        row = loc[0] + 1
        col = loc[1]
        
        #forward moves on column wise            
        "forward moves"
        while row < self.row_lim:            
            if(self.board[row][col]!=0):
                break
            
            #moves.append((col,row))
            moves.append((row,col))
            row+=1
        
        #backward moves row wise
        row = loc[0]
        col = loc[1] - 1
        while col >=0:
            if(self.board[row][col]!=0):
                break
            #moves.append((col,row))
            moves.append((row,col))
            col-=1
        
        #back ward moves column wise
        row = loc[0] - 1
        col = loc[1] 
        #Column wise backward moves
        while row >=0:
            if(self.board[row][col]!=0):
                break
            #moves.append((col,row))
            moves.append((row,col))
            row-=1
                
        #diagonal forward moves row ++ col++
        i,j = loc[0]+1,loc[1]+1
        while((j < self.col_lim) and (i < self.row_lim) ):
           "column wise forward moves"            
           if self.board[i][j]!=0:
               break           
           #moves.append((j,i))
           moves.append((i,j))
           i+=1
           j+=1
        
        #diagonal backword row-- col --
        i,j = loc[0]-1,loc[1]-1
        while((i >= 0) and (j >= 0)):
            "column wise forward moves"            
            if self.board[i][j]!=0:
                break
            #if [i,j] not in moves:
            #moves.append((j,i))
            moves.append((i,j))
            i-=1
            j-=1
            
        #diagonal forward moves row ++ col--
        i,j = loc[0]+1,loc[1]-1
        while((j >=0) and (i < self.row_lim) ):
           "column wise forward moves"            
           if self.board[i][j]!=0:
               break           
           #moves.append((j,i))
           moves.append((i,j))
           i+=1
           j-=1
        
        #diagonal backword row-- col ++
        i,j = loc[0]-1,loc[1]+1
        while((i >= 0) and (j < self.col_lim)):
            "column wise forward moves"            
            if self.board[i][j]!=0:
                break
            #if [i,j] not in moves:
            #moves.append((j,i))
            moves.append((i,j))
            i-=1
            j+=1
            
        return list(set(moves))
    
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
        #from copy import deepcopy
        #check if the move is legal
        print("move",move)
        print("board before move ", self.board)
        legal_moves = self.get_legal_moves()
        print("legal_moves =",legal_moves)
        if move not in legal_moves:        
            raise RuntimeError("Illegal move")
        
        #self.initiator ^= 1
        #self.player_loc[self.initiator]=move
        #create a new board
        nboard = deepcopy(self)
        print("board after deepcopy ", nboard.board)
        #block the last box
        nboard.board[move[0]][move[1]] = 1
        #nboard.board[move[1]][move[0]] = 1 #moves are in column row order
        nboard.player_loc[self.initiator]=move#moves are column,row order
        nboard.initiator ^=1
        
        print("board after move ",nboard.board)
        
        return nboard