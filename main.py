import pygame
from pygame.constants import MOUSEBUTTONDOWN

pygame.init()

B_rook = pygame.transform.scale(pygame.image.load(r"img\\BlackRook.png"), (65, 65))
B_knight = pygame.transform.scale(pygame.image.load(r"img\\BlackKnight.png"),(65, 65))
B_bishop = pygame.transform.scale(pygame.image.load(r"img\\BlackBishop.png"), (65, 65))
B_king = pygame.transform.scale(pygame.image.load(r"img\\BlackKing.png"), (65, 65))
B_queen = pygame.transform.scale(pygame.image.load(r"img\\BlackQueen.png"), (65, 65))
B_pawn = pygame.transform.scale(pygame.image.load(r"img\\BlackPawn.png"), (65, 65))

W_rook = pygame.transform.scale(pygame.image.load(r"img\\WhiteRook.png"), (65, 65))
W_knight = pygame.transform.scale(pygame.image.load(r"img\\WhiteKnight.png"), (65, 65))
W_bishop = pygame.transform.scale(pygame.image.load(r"img\\WhiteBishop.png"), (65, 65))
W_king = pygame.transform.scale(pygame.image.load(r"img\\WhiteKing.png"), (65, 65))
W_queen = pygame.transform.scale(pygame.image.load(r"img\\WhiteQueen.png"), (65, 65))
w_pawn = pygame.transform.scale(pygame.image.load(r"img\\WhitePawn.png"), (65, 65))

Board = pygame.transform.scale(pygame.image.load(r"img\\board.png"), (800, 600))

width = 800
height = 600

W = [W_rook, W_knight, W_bishop, W_king, W_queen, w_pawn]
B = [B_rook, B_knight, B_bishop, B_king, B_queen, B_pawn]

def display_piece():
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] != 0:
                screen.blit(board[i][j], ((j*100)+16,(i*75)+10))

def move(x, y):
    X1 = x
    Y1 = y
    x = valid_moves.prev[0]
    y = valid_moves.prev[1]

    if((board[y][x] in W and board[Y1][X1] in W) or (board[y][x] in B and board[Y1][X1] in B)):
        print("Invalid move")
        return not white
    else:
        if(white):
            if(board[y][x] in W):
                temp = board[y][x]
                board[y][x] = 0
                board[Y1][X1] = temp
                print(y, x,">", Y1, X1)
                valid_moves.selected.clear()
                return True
            else:
                valid_moves.selected.clear()
                print("White's turn")
        else:
            if(board[y][x] in B):
                temp = board[y][x]
                board[y][x] = 0
                board[Y1][X1] = temp
                print(y, x,">", Y1, X1)
                valid_moves.selected.clear()
                return False
            else:
                valid_moves.selected.clear()
                print("black's turn")
                return True

def draw():
    for i in range(len(valid_moves.selected)):
        x, y = valid_moves.selected[i]
        pygame.draw.circle(screen, (255, 0, 0), ((y*100)+50, (x*75)+35), 15)

class valid_moves:

    prev = (0, 0)
    selected = []
    king_moves = (0,0)

    def pawn(x, y, c):
        # method to all possible moves of pawn
        if c == "b":
            if y+2 <= 7:
                if y == 1 and board[y+2][x] == 0:
                    valid_moves.selected.append((y+1,x))
                    valid_moves.selected.append((y+2, x))
            if y+1 <= 7 and x+1 <= 7:
                if board[y+1][x+1] in W:
                    valid_moves.selected.append((y+1,x+1))
            if y+1 <= 7 and x-1 >=0:
                if board[y+1][x-1] in W:
                    valid_moves.selected.append((y+1,x-1))
            if y+1 <= 7:
                if(board[y+1][x] == 0):
                    valid_moves.selected.append((y+1, x))
        else:
            if y-2 >= 0:
                if y == 6 and board[y-2][x] == 0:
                    valid_moves.selected.append((y-1, x))
                    valid_moves.selected.append((y-2, x))
            if y-1 >= 0 and x-1 >= 0:
                if board[y-1][x-1] in B:
                    valid_moves.selected.append((y-1,x-1))
            if y-1 >= 0 and x+1 <= 7:
                if board[y-1][x+1] in B:
                    valid_moves.selected.append((y-1,x+1))
            if y-1 >= 0:
                if(board[y-1][x] == 0):
                    valid_moves.selected.append((y-1, x))

    def knight(x, y, c):
        #mrthod for all possible moves of knight
        if c == "b":
            #bottom right
            if y+2 <= 7 and x+1 <= 7:
                if board[y+2][x+1] == 0 or board[y+2][x+1] in W:
                    valid_moves.selected.append((y+2, x+1))

            #up right
            if y-2 >= 2 and x-1 >= 0:
                if board[y-2][x-1] == 0 or board[y-2][x-1] in W:
                    valid_moves.selected.append((y-2, x-1))

            #bottom left
            if y+2 <= 7 and x-1 >= 0:
                if board[y+2][x-1] == 0 or board[y+2][x-1] in W:
                    valid_moves.selected.append((y+2, x-1))

            #up left
            if y-2 >= 0 and x+1 <= 7:
                if board[y-2][x+1] == 0 or board[y-2][x+1] in W:
                    valid_moves.selected.append((y-2, x+1))
            
            #left bottom 
            if y+1 <= 7 and x-2 >= 0:
                if board[y+1][x-2] == 0 or board[y+1][x-2] in W:
                    valid_moves.selected.append((y+1, x-2))

            #left up
            if y-1 >= 0 and x-2 >= 0:
                if board[y-1][x-2] == 0 or board[y-1][x-2] in W:
                    valid_moves.selected.append((y-1, x-2))

            #right bottom
            if y+1 <= 7 and x+2 <= 7:
                if board[y+1][x+2] == 0 or board[y+1][x+2] in W:
                    valid_moves.selected.append((y+1, x+2))

            #right up
            if y-1 >= 0 and x+2 <= 7:
                if board[y-1][x+2] == 0 or board[y-1][x+2] in W:
                    valid_moves.selected.append((y-1, x+2))

        else:
            #up right
            if y-2 >= 0 and x-1 >= 0:
                if board[y-2][x-1] == 0 or board[y-2][x-1] in B:
                    valid_moves.selected.append((y-2, x-1))

            #bottom right
            if y+2 <= 7 and x+1 <= 7:
                if board[y+2][x+1] == 0 or board[y+2][x+1] in B:
                    valid_moves.selected.append((y+2, x+1))

            #bottom left
            if y+2 <= 7 and x-1 >= 0:
                if board[y+2][x-1] == 0 or board[y+2][x-1] in B:
                    valid_moves.selected.append((y+2, x-1))

            #up left
            if y-2 >= 0 and x+1 <= 7:
                if board[y-2][x+1] == 0 or board[y-2][x+1] in B:
                    valid_moves.selected.append((y-2, x+1))
            
            #left bottom 
            if y+1 <= 7 and x-2 >= 0:
                if board[y+1][x-2] == 0 or board[y+1][x-2] in B:
                    valid_moves.selected.append((y+1, x-2))

            #left up
            if y-1 >= 0 and x-2 >= 0:
                if board[y-1][x-2] == 0 or board[y-1][x-2] in B:
                    valid_moves.selected.append((y-1, x-2))

            #right bottom
            if y+1 <= 7 and x+2 <= 7:
                if board[y+1][x+2] == 0 or board[y+1][x+2] in B:
                    valid_moves.selected.append((y+1, x+2))

            #right up
            if y-1 >= 0 and x+2 <= 7:
                if board[y-1][x+2] == 0 or board[y-1][x+2] in B:
                    valid_moves.selected.append((y-1, x+2))

    def rook(x, y, c):
        if c == "b":
            #right
            for i in range(x+1, 8):
                if board[y][i] == 0:
                    valid_moves.selected.append((y, i))
                    if i+1 <= 7:
                        if board[y][i+1] in W:
                            valid_moves.selected.append((y, i+1))
                            break
                elif board[y][i] in W:
                    valid_moves.selected.append((y, i))
                    break
                else:
                    break

            #left
            for i in range(x-1, -1, -1):
                if board[y][i] == 0:
                    valid_moves.selected.append((y, i))
                    if i-1 >= 0:
                        if board[y][i-1] in W:
                            valid_moves.selected.append((y, i-1))
                            break
                elif board[y][i] in W:
                    valid_moves.selected.append((y, i))
                    break
                else:
                    break

            #down
            for i in range(y+1, 8):
                if board[i][x] == 0:
                    valid_moves.selected.append((i, x))
                    if i+1 <= 7:
                        if board[i+1][x] in W:
                            valid_moves.selected.append((i+1, x))
                            break
                elif board[i][x] in W:
                    valid_moves.selected.append((i, x))
                    break
                else:
                    break

            #up
            for i in range(y-1, -1, -1):
                if board[i][x] == 0:
                    valid_moves.selected.append((i, x))
                    if i-1 >= 0:
                        if board[i-1][x] in W:
                            valid_moves.selected.append((i-1, x))
                            break
                elif board[i][x] in W:
                    valid_moves.selected.append((i, x))
                    break
                else:
                    break
        
        else:
            #right
            for i in range(x+1, 8):
                if board[y][i] == 0:
                    valid_moves.selected.append((y, i))
                    if i+1 <= 7:
                        if board[y][i+1] in B:
                            valid_moves.selected.append((y, i+1))
                            break
                elif board[y][i] in B:
                    valid_moves.selected.append((y, i))
                    break
                else:
                    break

            #left
            for i in range(x-1, -1, -1):
                if board[y][i] == 0:
                    valid_moves.selected.append((y, i))
                    if i-1 >= 0:
                        if board[y][i-1] in B:
                            valid_moves.selected.append((y, i-1))
                            break
                elif board[y][i] in B:
                    valid_moves.selected.append((y, i))
                    break
                else:
                    break

            #down
            for i in range(y+1, 8):
                if board[i][x] == 0:
                    valid_moves.selected.append((i, x))
                    if i+1 <= 7:
                        if board[i+1][x] in B:
                            valid_moves.selected.append((i+1, x))
                            break
                elif board[i][x] in B:
                    valid_moves.selected.append((i, x))
                    break
                else:
                    break

            #up
            for i in range(y-1, -1, -1):
                if board[i][x] == 0:
                    valid_moves.selected.append((i, x))
                    if i-1 >= 0:
                        if board[i-1][x] in B:
                            valid_moves.selected.append((i-1, x))
                            break
                elif board[i][x] in B:
                    valid_moves.selected.append((i, x))
                    break
                else:
                    break

    
    def bishop(x, y, c):
        if c == "b":

            #Down right cross
            i = x 
            j = y
            while(i < 7 and j < 7):
                i = i+1
                j = j+1
                if board[j][i] == 0:
                    valid_moves.selected.append((j, i))
                    if j+1 < 8 and i+1 < 8:
                        if board[j+1][i+1] in W:
                            valid_moves.selected.append((j+1, i+1))
                            break
                else:
                    break

            #Down left cross
            i = x 
            j = y
            while(i > 0 and j < 7):
                i = i-1
                j = j+1
                if board[j][i] == 0:
                    valid_moves.selected.append((j, i))
                    if j+1 < 8 and i-1 >= 0:
                        if board[j+1][i-1] in W:
                            valid_moves.selected.append((j+1, i-1))
                            break
                else:
                    break

            #Up left cross
            i = x 
            j = y
            while(i > 0 and j > 0):
                i = i-1
                j = j-1
                if board[j][i] == 0:
                    valid_moves.selected.append((j, i))
                    if j-1 >= 0 and i-1 >= 0:
                        if board[j-1][i-1] in W:
                            valid_moves.selected.append((j-1, i-1))
                            break
                else:
                    break

            #Up right cross
            i = x
            j = y
            while(i < 7 and j > 0):
                i = i+1
                j = j-1
                if board[j][i] == 0:
                    valid_moves.selected.append((j, i))
                    if i+1 < 8 and j-1 >= 0:
                        if board[j-1][i+1] in W:
                            valid_moves.selected.append((j-1, i+1))
                            break
                else:
                    break


        else:

            #Up left cross
            i = x 
            j = y
            while(i > 0 and j > 0):
                i = i-1
                j = j-1
                if board[j][i] == 0:
                    valid_moves.selected.append((j, i))
                    if j-1 >= 0 and i-1 >= 0:
                        if board[j-1][i-1] in B:
                            valid_moves.selected.append((j-1, i-1))
                            break
                else:
                    break

            #Up right cross
            i = x
            j = y
            while(i < 7 and j > 0):
                i = i+1
                j = j-1
                if board[j][i] == 0:
                    valid_moves.selected.append((j, i))
                    if i+1 < 8 and j-1 >= 0:
                        if board[j-1][i+1] in B:
                            valid_moves.selected.append((j-1, i+1))
                            break
                else:
                    break

            #Down right cross
            i = x 
            j = y
            while(i < 7 and j < 7):
                i = i+1
                j = j+1
                if board[j][i] == 0:
                    valid_moves.selected.append((j, i))
                    if j+1 < 8 and i+1 < 8:
                        if board[j+1][i+1] in B:
                            valid_moves.selected.append((j+1, i+1))
                            break
                else:
                    break

            #Down left cross
            i = x 
            j = y
            while(i > 0 and j < 7):
                i = i-1
                j = j+1
                if board[j][i] == 0:
                    valid_moves.selected.append((j, i))
                    if j+1 < 8 and i-1 >= 0:
                        if board[j+1][i-1] in B:
                            valid_moves.selected.append((j+1, i-1))
                            break
                else:
                    break

    def king(x, y, c):
        if c == "b":
            
            #Down
            if y+1 < 8:
                if board[y+1][x] == 0 or board[y+1][x] in W:
                    valid_moves.selected.append((y+1, x))
            
            #up
            if y-1 >= 0:
                if board[y-1][x] == 0 or board[y-1][x] in W:
                    valid_moves.selected.append((y-1, x))

            #Left
            if x-1 >= 0:
                if board[y][x-1] == 0 or board[y][x-1] in W:
                    valid_moves.selected.append((y, x-1))

            #Right
            if x+1 < 8:
                if board[y][x+1] == 0 or board[y][x+1] in W:
                    valid_moves.selected.append((y, x+1))

            #Up Left
            if x-1 >= 0 and y-1 >= 0:
                if board[y-1][x-1] == 0 or board[y-1][x-1] in W:
                    valid_moves.selected.append((y-1, x-1))

            #up right
            if y-1 >= 0 and x+1 < 8:
                if board[y-1][x+1] == 0 or board[y-1][x+1] in W:
                    valid_moves.selected.append((y-1, x+1))

            #Down Left
            if x-1 >= 0 and y+1 < 8:
                if board[y+1][x-1] == 0 or board[y+1][x-1] in W:
                    valid_moves.selected.append((y+1, x-1))

            #Down Right
            if x+1 < 8 and y+1 < 8:
                if board[y+1][x+1] == 0 or  board[y+1][x+1] in W:
                    valid_moves.selected.append((y+1, x+1))

        else:
            
            #Down
            if y+1 < 8:
                if board[y+1][x] == 0 or board[y+1][x] in B:
                    valid_moves.selected.append((y+1, x))
            
            #up
            if y-1 >= 0:
                if board[y-1][x] == 0 or board[y-1][x] in B:
                    valid_moves.selected.append((y-1, x))

            #Left
            if x-1 >= 0:
                if board[y][x-1] == 0 or board[y][x-1] in B:
                    valid_moves.selected.append((y, x-1))

            #Right
            if x+1 < 8:
                if board[y][x+1] == 0 or board[y][x+1] in B:
                    valid_moves.selected.append((y, x+1))

            #Up Left
            if x-1 >= 0 and y-1 >= 0:
                if board[y-1][x-1] == 0 or board[y-1][x-1] in B:
                    valid_moves.selected.append((y-1, x-1))

            #up right
            if y-1 >= 0 and x+1 < 8:
                if board[y-1][x+1] == 0 or board[y-1][x+1] in B:
                    valid_moves.selected.append((y-1, x+1))

            #Down Left
            if x-1 >= 0 and y+1 < 8:
                if board[y+1][x-1] == 0 or board[y+1][x-1] in B:
                    valid_moves.selected.append((y+1, x-1))

            #Down Right
            if x+1 < 8 and y+1 < 8:
                if board[y+1][x+1] == 0 or board[y+1][x+1] in B:
                    valid_moves.selected.append((y+1, x+1))
        
        valid_moves.king_moves = (valid_moves.selected, c)

    def queen(x, y, c):
        if c == "b":
            valid_moves.rook(x, y, "b")
            valid_moves.bishop(x, y, "b")
        else:
            valid_moves.rook(x, y, "w")
            valid_moves.bishop(x, y, "w")


    #valid moves are stored in selected
    def valid_piece(x, y):
        valid_moves.selected.clear()

        if not white:
            #moves of balck pieces
            if B_pawn == board[y][x]:
                valid_moves.pawn(x, y, "b")
            elif B_knight == board[y][x]:
                valid_moves.knight(x, y, "b")
            elif B_rook == board[y][x]:
                valid_moves.rook(x, y, "b")
            elif B_bishop == board[y][x]:
                valid_moves.bishop(x, y, "b")
            elif B_king == board[y][x]:
                valid_moves.king(x, y, "b")
            elif B_queen == board[y][x]:
                valid_moves.queen(x, y, "b")
        else:
            #moves of white pieces
            if w_pawn == board[y][x]:
                valid_moves.pawn(x, y, "w")
            elif W_knight == board[y][x]:
                valid_moves.knight(x, y, "w")
            elif W_rook == board[y][x]:
                valid_moves.rook(x, y, "w")
            elif W_bishop == board[y][x]:
                valid_moves.bishop(x, y, "w")
            elif W_king == board[y][x]:
                valid_moves.king(x, y, "w")
            elif W_queen == board[y][x]:
                valid_moves.queen(x, y, "w")

def check_mate():
    if valid_moves.king_moves[0] == valid_moves.selected:
        if valid_moves.king_moves[1] == "b":
            print("White wins")
        else:
            print("Black wins")

board = [[B_rook, B_knight, B_bishop, B_queen, B_king, B_bishop, B_knight, B_rook],
        [B_pawn, B_pawn, B_pawn, B_pawn, B_pawn, B_pawn, B_pawn, B_pawn],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], 
        [w_pawn, w_pawn, w_pawn, w_pawn, w_pawn, w_pawn, w_pawn, w_pawn], 
        [W_rook, W_knight, W_bishop, W_queen, W_king, W_bishop, W_knight, W_rook]]

white = True
def main():
    run = True
    global white
    while run:
        screen.blit(Board, (0,0))
        display_piece()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                m = True
                x, y = pygame.mouse.get_pos()

                x = int(x/100)
                y = int(y/75)

                if(len(valid_moves.selected) != 0):
                    if x == valid_moves.prev[0] and y == valid_moves.prev[1]:
                        valid_moves.selected.clear()
                    for i in range(len(valid_moves.selected)):
                        if((y, x) == valid_moves.selected[i]):
                            m = move(x, y)
                            check_mate()
                            if m:
                                white = False
                            else:
                                white = True
                            break
                else:
                    valid_moves.prev = (x, y)
                    valid_moves.valid_piece(x, y)
                    break

        draw()
        pygame.display.update()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chess')
main()