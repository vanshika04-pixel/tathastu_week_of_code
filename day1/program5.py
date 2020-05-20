run_player1=int(input("enter the runs scored by first player:"))
run_player2=int(input("enter the runs scored by second player"))
run_player3=int(input("enter the runs scored by third player"))
strike_rate1=run_player1*100/60
strike_rate2=run_player2*100/60
strike_rate3=run_player3*100/60
print("strike rate of player 1 is:",strike_rate1)
print("strike rate of player 2 is:",strike_rate2)
print("strike rate of plalyer 3 is:",strike_rate3)
print("runs scored by player 1 if they played 60 more balls is",run_player1*2)
print("runs scored by player 2 if they had played 60 more balls is",run_player2*2)
print("'runs scored by player 3 if they had played 60 more balls is",run_player3)
print("maximum number of sixes player 1 could hit=",run_player1//6)
print("maximum number of sixes player 2 could hit=",run_player2//6)
print("maximum number of sixes player 3 could hit=",run_player3//6)
