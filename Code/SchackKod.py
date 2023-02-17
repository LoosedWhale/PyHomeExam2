#Note that this is a mock up of what for the games features.
#Not actual code for a Chess game.

import tkinter

# Create a window
root = tkinter.Tk()
root.title("Chess")
root.geometry("400x400")
root.resizable(False, False)

# Create a 8x8 grid
class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        
    def updatePiece(self, piece):
        self.piece = piece

# define a base class for all pieces
class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        
    def move(self, newPosition):
        self.position = newPosition

# define a class for pawn
class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def move(self, newPosition):
        pass

# define a class for knight
class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def move(self, newPosition):
        pass

# define a class for bishop

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def move(self, newPosition):
        pass

# define a class for rook
class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def move(self, newPosition):
        pass
# define a class for queen
class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def move(self, newPosition):
        pass
# define a class for king
class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def move(self, newPosition):
        pass

# define a class for the chess board and set up the pieces on the board. 
class ChessBoard:
    def __init__(self):
        self.board = [[Square(i, j) for j in range(8)] for i in range(8)]
        
        for col in range(8):
            self.board[1][col].updatePiece(Pawn('black', (1, col)))
            self.board[6][col].updatePiece(Pawn('white', (6, col)))
        
        self.board[0][0].updatePiece(Rook('black', (0, 0)))
        self.board[0][7].updatePiece(Rook('black', (0, 7)))
        self.board[7][0].updatePiece(Rook('white', (7, 0)))
        self.board[7][7].updatePiece(Rook('white', (7, 7)))
        
        self.board[0][1].updatePiece(Knight('black', (0, 1)))
        self.board[0][6].updatePiece(Knight('black', (0, 6)))
        self.board[7][1].updatePiece(Knight('white', (7, 1)))
        self.board[7][6].updatePiece(Knight('white', (7, 6)))
        
        self.board[0][2].updatePiece(Bishop('black', (0, 2)))
        self.board[0][5].updatePiece(Bishop('black', (0, 5)))
        self.board[7][2].updatePiece(Bishop('white', (7, 2)))
        self.board[7][5].updatePiece(Bishop('white', (7, 5)))

        self.board[0][3].updatePiece(Queen('black', (0, 3)))
        self.board[7][3].updatePiece(Queen('white', (7, 3)))

        self.board[0][4].updatePiece(King('black', (0, 4)))
        self.board[7][4].updatePiece(King('white', (7, 4)))

        self.canvas = tkinter.Canvas(root, width=400, height=400)
        self.canvas.pack()
        
    def display(self):
        squareSize = 50
        x, y = 0, 0
        
        for row in self.board:
            for square in row:
                if (square.row + square.col) % 2 == 0:
                    color = 'white'
                else:
                    color = 'light grey'
                    
                self.canvas.create_rectangle(x, y, x+squareSize, y+squareSize, fill=color)
                
                if square.piece:
                    if square.piece.color == 'black':
                        color = 'black'
                    else:
                        color = 'white'
                    self.canvas.create_oval(x, y, x+squareSize, y+squareSize, fill=color)
                
                x += squareSize
            x = 0
            y += squareSize


# define a class for the square
chessBoard = ChessBoard()
chessBoard.display()
root.mainloop()
