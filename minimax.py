from minimax_helpers import *


def minimax_decision(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """
    # TODO: Finish this function!
    #initialize variables
    temp_val = float('-inf')
    r_mov = None
    r_val = temp_val
    legal_moves = gameState.get_legal_moves()
    for mov  in legal_moves:
        temp_val= max(temp_val,min_value(gameState.forecast_move(mov)))
        if temp_val > r_val:
            r_val = temp_val
            r_mov = mov
    
    return r_mov
