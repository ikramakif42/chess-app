def showBoardFEN(state="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
    pieces, turn, castling, enPassant, halfmove, fullmove = state.split()
    print(pieces, turn, castling, enPassant, halfmove, fullmove)
    pieces = pieces.split("/")
    
    r = 8
    for rank in pieces:
        print("  " + "+---"*8 + "+")
        print(r, end=" ")
        for i in rank:
            if i.isalpha():
                print(f"| {i} ", end="")
            else:
                print(f"|   "*int(i), end="")
        r -= 1
        print("|")
    print("  "+"+---"*8+"+")
    print("    "+"   ".join(chr(i) for i in range(65, 73)))


def showBoard(state):
    r = 8
    for rank in state["pieces"]:
        print("  " + "+---"*8 + "+")
        print(r, end=" ")
        for cell in rank:
            print(f"| {cell} ", end="")
        print("|")
        r -= 1
    print("  "+"+---"*8+"+")
    print("    "+"   ".join(chr(i) for i in range(65, 73)))


def makeMove(state, move):
    # Pawn push
    if len(move) == 2:
        file, rank = ord(move[0])-97, 8-int(move[1])
        t = 1 if state["turn"] == "w" else -1
        if state["pieces"][rank+t][file] != "p" and state["pieces"][rank+t][file] != "P":
            t *= 2
            if state["pieces"][rank+t][file] != "p" and state["pieces"][rank+t][file] != "P":
                print("???")
                return state
        print("\nMove:", move, "Turn:", state["turn"])
        print(rank, file, t, "\n")
        state["pieces"][rank][file] = state["pieces"][rank+t][file]
        state["pieces"][rank+t][file] = " "
        state["turn"] = "b" if state["turn"] == "w" else "w"
    
    # Other pieces move
    elif len(move) == 3:
        pass
    
    # Pawn Capture
    elif move[0] in ["a", "b", "c", "d", "e", "f", "g", "h"] and move[1] == "x":
        if len(move.split()) > 1:
            move, _ = move.split()
        fileFrom, file, rank = ord(move[0])-97, ord(move[2])-97, 8-int(move[3])
        t = 1 if state["turn"] == "w" else -1
        rankFrom = rank + t
        print(rank, file, rankFrom, fileFrom)
        if not (state["pieces"][rankFrom][fileFrom] == "P" and state["turn"] == "W") and not {
            state["pieces"][rankFrom][fileFrom] == "p" and state["turn"] == "b"
        }:
            print("???")
            return state
        if (state["pieces"][rankFrom][file] == "P" or state["pieces"][rankFrom][file] == "P") and (
            state["pieces"][rank][file] == " "):
            print("EN PASSANT")
            state["pieces"][rankFrom][file] = " "
        state["pieces"][rank][file] = state["pieces"][rankFrom][fileFrom]
        state["pieces"][rankFrom][fileFrom] = " "
        state["turn"] = "b" if state["turn"] == "w" else "w"

    # Other pieces move
    elif len(move) == 3:
        piece, file, rank = move[0], ord(move[1])-97, 8-int(move[2])
        pass

    # Special cases
    elif len(move.split()) > 1:
        move, extra = move.split()
        if extra == "+":
            print("Check!")
        elif extra == "#" or extra == "++":
            print("Checkmate")
        elif extra == "=" or extra == "(=)":
            print("Draw")

    
    return state

def loadMoves(state, moves):
    for i in moves:
        state = makeMove(state, i)
    return state





state = {
    "pieces" : [["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p" for i in range(8)],
    [" " for i in range(8)],
    [" " for i in range(8)],
    [" " for i in range(8)],
    [" " for i in range(8)],
    ["P" for i in range(8)],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]],

    "turn": "w"
}

state2 = {
    "pieces" : [["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", " ", "p", " "],
    [" " for i in range(8)],
    [" ", " ", " ", "P", " ", " ", " ", " "],
    [" ", "P", " ", " ", "Q", "p", " ", "p"],
    [" ", " ", " ", " ", "P", " ", " ", " "],
    ["P", " ", "P", " ", " ", "P", "P", "P"],
    ["R", "N", "B", " ", "K", "B", "N", "R"]],

    "turn": "b"
}

# state = loadMoves(state, ["d4", "h6", "d5", "e5"])
# state = makeMove(state, "d4")
# state = makeMove(state, "h6")
# state = makeMove(state, "d5")
# state = makeMove(state, "e5")

while True:
    print(f"{'-- White' if state['turn']=='w' else '-- Black'} to move -- ")
    showBoard(state)
    x = input()
    if x == "0":
        break
    else:
        state = makeMove(state, x)

# showBoardFEN()