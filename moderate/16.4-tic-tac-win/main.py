# Design an algorithm to figure out if someone has won a game of tic-tac-toe.

#Requisit the gameboard is **always** a square NxN
def won(game):
    for i in range(len(game)):
        #Rows
        if equal3(game[i][0],game[i][1], game[i][2]):
            return (game[i][0], "Row {}".format(i))

        #Columns
        if equal3(game[0][i],game[1][i], game[2][i]):
            return (game[0][i], "Columns {}".format(i))
    #Diagonal
    if equal3(game[0][0],game[1][1],game[2][2]):
        return (game[1][1], "Diagonal Desc")
    if equal3(game[2][0],game[1][1],game[0][2]):
        return (game[1][1], "Diagonal Asc")
    
    return False
        

def equal3(p1, p2, p3):
    if p1 == p2 and p2 == p3:
        return True
    return False


game1 = [["X","O","O"],
         ["X","O","O"],
         ["X","O","O"],
        ]
game2 = [["X","O","O"],
         ["X","X","O"],
         ["O","O","X"],
        ]

game3 = [["X","O","O"],
         ["O","O","X"],
         ["X","X","O"],
        ]

game4 = [["X","X","X"],
         ["O","O","O"],
         ["O","O","O"],
        ]


game5 = [["X","X","O"],
         ["O","O","X"],
         ["O","X","X"],
        ]
print(won(game1))
print(won(game2))
print(won(game3))
print(won(game4))
print(won(game5))