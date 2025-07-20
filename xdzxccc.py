import random

def play_cricket():
    print("Welcome to Python Cricket Game!")
    print("You are batting. Try to score as many runs as possible.")

    total_runs = 0
    wickets = 0
    total_balls = 6
    while total_balls > 0 and wickets < 3:
        input("Press Enter to bat...")
        computer_bowl = random.randint(1, 6)
        your_shot = int(input("Enter your shot (1-6): "))
        if your_shot < 1 or your_shot > 6:
            print("Invalid shot! Try again.")
            continue
        
        print("Computer bowls:", computer_bowl)
        if computer_bowl == your_shot:
            print("OUT! You're bowled!")
            wickets += 1
        else:
            total_runs += your_shot
            print("You scored", your_shot, "runs!")
        
        print("Your total runs:", total_runs, "for", wickets, "wickets.")
        total_balls -= 1

    print("Innings over!")
    print("You scored", total_runs, "runs for", wickets, "wickets in", 6 - total_balls, "overs.")
    print("Game Over!")

play_cricket()
