board = "   |   |   \n---+---+---\n   |   |   \n---+---+---\n   |   |   "

wining_pos=[[1,2,3],[1,4,7],[1,5,9],[4,5,6],[7,8,9],[2,5,8],[3,6,9],[3,5,7]]
p1=set()  #X
p2=set()  #O

positions = {
    1: 1,   # top-left
    2: 5,   # top-middle
    3: 9,   # top-right
    4: 25,  # mid-left
    5: 29,  # center
    6: 33,  # mid-right
    7: 49,  # bottom-left
    8: 53,  # bottom-middle
    9: 57   # bottom-right
}


def chk(player:set):
    for i in wining_pos:
        if(set(i).issubset(player)):
            return True
    else:
        return False

def chkWinDraw():
    if(len(p1)==5 or len(p2)==5):
        print("Draw")
        return True
    elif(chk(p1)):
        print("Player 1 Wins")
        return True
    elif(chk(p2)):
        print("Player 2 Wins")
        return True
    

def takeinput(player :set,ch):
    global board
    pos=int(input(f"Enter Position player {ch}: "))
    if(pos in positions.keys() and board[positions[pos]]==" "):
        player.add(pos)
        board = board[:positions[pos]] + ch + board[positions[pos]+1:]
        return
    else:
        print("invaled Position try again")
        takeinput(player,ch)

while True:
    print(board)
    if(chkWinDraw()):
        break  
    takeinput(p1,"X") 

    print(board)
    if(chkWinDraw()):
        break  
    takeinput(p2,"O")
