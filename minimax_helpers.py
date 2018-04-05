
def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    # TODO: finish this function!
    legal_moves = gameState.get_legal_moves()
    #print("legal_moves ",legal_moves)
    if len(legal_moves) == 0:
        return True
    
    return False


def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    # TODO: finish this function!
    if terminal_test(gameState):
        return 1
    
    #define the minimum val    
    min_val = float('inf')
    
    #find the minimum from remaining moves
    legal_moves = gameState.get_legal_moves()
    for move in legal_moves:
    #for move in gameState.get_legal_moves():
        min_val=min(min_val,max_value(gameState.forecast_move(move)))
    return min_val

def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    # TODO: finish this function!
    #test if the game ended, by checking the available moves
    if terminal_test(gameState):
        return -1
    
    #initialize a max_val
    max_val = float('-inf')
    #if the state is not terminal then find the max val from the moves
    legal_moves = gameState.get_legal_moves()
    for move in legal_moves:
    #for move in gameState.get_legal_moves():
        max_val=max(max_val,min_value(gameState.forecast_move(move)))
    
    return max_val

