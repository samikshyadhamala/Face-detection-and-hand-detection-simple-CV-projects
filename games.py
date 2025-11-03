# # lista=[1,2,3,4,5,6,7,8,9]
# # def list_print(b):
# #     for i in b:
# #         a=print(i)
# #         if len(a)==3:
# #             print(a)
# # # list_print(lista)
# # list_print(lista)



# board=[" "," "," "," "," "," "," "," "," "]
# def print_board():
#     print("Current Board:")
#     print(f"{board[0]} | {board[1]} | {board[2]}")
#     print("---------")
#     print(f"{board[3]} | {board[4]} | {board[5]}")
#     print("---------")
#     print(f"{board[6]} | {board[7]} | {board[8]}")
#     print("\n")


#     print_board()
#     for i in range(1,10):
#             # move = int(move)
#             print(i)
            
#             if board!= [" ", " ", " ", " ", " ", " ", " ", " ", " "] and i == 1:
#                 print("Game already in progress, do you want to start a new game? (yes/no)")
#                 response = str(input("Enter your response: ")).strip().lower()
#                 if response == "yes":
#                     board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
#                 else:
#                     print("quiting the game ")
#                     break
            
#             if i%2==0:
#                 print("player 1's turn")
#                 move=int(input("Enter your move (1-9): "))
#                 if move < 1 or move > 9:
#                     print("Invalid move, please enter a number between 1 and 9.")
#                     continue
#                 if board[move-1] == " ":
#                     board[move-1] = "X"
#                 else:
#                     print("already taken")
#                     continue
#             else:
#                 print("player 2's turn")
#                 move=int(input("Enter your move (1-9): "))
#                 if move <1 or move>9:
#                     print("invalid move please enter a number between 1 and 9.")
#                     continue
#                 if board[move-1] == " ":
#                     board[move-1] = "O"
#                 else:
#                     print("already taken")
#                     continue
#             # if board == [" ", " ", " ", " ", " ", " ", " ", " ", " "] and i == 1:
#             #     print("new game ")
#             if (board[0] == board[1] == board[2] != " ") or \
#                (board[3] == board[4] == board[5] != " ") or \
#                (board[6] == board[7] == board[8] != " ") or \
#                (board[0] == board[3] == board[6] != " ") or \
#                (board[1] == board[4] == board[7] != " ") or \
#                (board[2] == board[5] == board[8] != " ") or \
#                (board[0] == board[4] == board[8] != " ") or \
#                (board[2] == board[4] == board[6] != " "):
#                 print(f"Player {'X' if i % 2 == 0 else 'O'} wins!")
                
#                 print(i)
#                 break   
#             if i==9:
#                 print("its a draw")       
#             i+=1 
# print_board()



