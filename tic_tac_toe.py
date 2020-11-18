coords = {
"a1": "_", 
"a2": "_",
"a3": "_",
"b1": "_",
"b2": "_",
"b3": "_",
"c1": " ",
"c2": " ",
"c3": " ",}
team = input("Play Tic-Tac-Toe! \n Choose team X or O: ").lower()

if team in ["x", "o"]:
    for i in range(9):
        print("Team " + team + " make a move!")
        print(f"  1 2 3 \nA {coords['a1']}|{coords['a2']}|{coords['a3']} \nB {coords['b1']}|{coords['b2']}|{coords['b3']} \nC {coords['c1']}|{coords['c2']}|{coords['c3']}" ) 
        move = input("Input cordinates (A1, B2 etc.): ").lower()
        coords[move] = team
        # while test == false:
        #     move = input("Input cordinates (A1, B2 etc.): ").lower()
        #     if coords[move] in ["x", "o"]
        #         test = False
        #     else
        #         test = True    
        print(f"  1 2 3 \nA {coords['a1']}|{coords['a2']}|{coords['a3']} \nB {coords['b1']}|{coords['b2']}|{coords['b3']} \nC {coords['c1']}|{coords['c2']}|{coords['c3']}" )  
        team = 'x' if team == 'o' else 'o' 
        # for coordinate == move == (coordinate) set (coordinate) to 'var team'x
    else:
        print("Winner is ") #+ winner)











# for i in range(2):
#     for i in range(6):
#         print("       |        |")
#     for i in range(1):
#         print ("------------------------")
# for i in range(6):
#         print("       |        |")

# \    / | ====== | ======      
#  \  /  | =    = | =    = 
#   \/   | =    = | =    =
#   /\   | =    = | =    =
#  /  \  | =    = | =    =
# /    \ | ====== | ======      
# ------------------------
# \    / | ====== | ======      
#  \  /  | =    = | =    = 
#   \/   | =    = | =    =
#   /\   | =    = | =    =
#  /  \  | =    = | =    =
# /    \ | ====== | ======      
# ------------------------
# \    / | ====== | ======      
#  \  /  | =    = | =    = 
#   \/   | =    = | =    =
#   /\   | =    = | =    =
#  /  \  | =    = | =    =
# /    \ | ====== | ======      

#  _|_|_
#  _|_|_
#   | | 

