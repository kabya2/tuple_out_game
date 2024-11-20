import random

def roll_dice():
    """Simulate rolling three dice."""
    return [random.randint(1, 6) for _ in range(3)]

def check_tuple(dice):
    """Check if all three dice are the same."""
    return len(set(dice)) == 1

def play_turn(player_name):
    """Simulate a player's turn."""
    print(f"\n{player_name}'s turn!")
    dice = roll_dice()
    print(f"Rolled: {dice}")
    
    while True:
        if check_tuple(dice):
            print(f"Tupled out! {player_name} scores 0 points this turn.")
            return 0

        # Fix dice with matching pairs
        fixed_dice = [die for die in dice if dice.count(die) > 1]
        print(f"Fixed dice: {fixed_dice}")
        
        # Allow re-rolling unfixed dice
        if len(fixed_dice) < 3:
            reroll = input("Do you want to re-roll the unfixed dice? (yes/no): ").strip().lower()
            if reroll == 'yes':
                unfixed_dice = [die for die in dice if die not in fixed_dice]
                new_roll = [random.randint(1, 6) for _ in range(len(unfixed_dice))]
                dice = fixed_dice + new_roll
                print(f"Re-rolled: {dice}")
            else:
                break
        else:
            break
    
    score = sum(dice)
    print(f"{player_name} ends their turn with {score} points.")
    return score

def main():
    print("Welcome to the 'Tuple Out' Dice Game!")
    player_count = int(input("Enter the number of players: "))
    players = {f"Player {i + 1}": 0 for i in range(player_count)}
    winning_score = 50

    while True:
        for player_name in players:
            score = play_turn(player_name)
            players[player_name] += score
            print(f"Current scores: {players}")

            if players[player_name] >= winning_score:
                print(f"\n{player_name} wins with {players[player_name]} points!")
                return

if __name__ == "__main__":
    main()
