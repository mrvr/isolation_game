from solution import *

print("Creating empty game board...")
g = GameState()

print("Getting legal moves for player 1...")
p1_empty_moves = g.get_legal_moves()
print("Found {} legal moves.".format(len(p1_empty_moves or [])))

print("Applying move (0, 0) for player 1...")
g1 = g.forecast_move((0, 0))
print("Getting legal moves for player 2...")
p2_empty_moves = g1.get_legal_moves()
print("p2_empty_moves =", p2_empty_moves)

if (0, 0) in set(p2_empty_moves):
    print("Failed\n  Uh oh! (0, 0) was not blocked properly when " +
          "player 1 moved there.")
else:
    print("Everything looks good!")
    
#g2 = g1.forecast_move((1, 0))
#print("Getting legal moves for player 1...")
#p3_empty_moves = g2.get_legal_moves()
#print("p3_empty_moves =", p3_empty_moves)
#
#if (1, 0) in set(p3_empty_moves):
#    print("Failed\n  Uh oh! (0, 0) was not blocked properly when " +
#          "player 1 moved there.")
#else:
#    print("Everything looks good!")